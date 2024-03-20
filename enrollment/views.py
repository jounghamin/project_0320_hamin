from django.shortcuts import render
from django.http import HttpResponse

from .models import Enrollment, Lecture
from .serializers import EnrollmentSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from lectures.serializers import Lecture
from students.serializers import Student


# Create your views here.

@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        enrollment = Enrollment.objects.all()
        serializer = EnrollmentSerializers(enrollment, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # instructor = Instructor.objects.get(id=id)
        #lecture id 키 
        data = request.data
        lecture_id = data.get('lecture_id')
        lecture = Lecture.objects.get(id=lecture_id)

        serializer = EnrollmentSerializers(data=data)

        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(lecture=lecture)
        #     return Response(serializer.data, status=201)
        #student id 키 
        # data = request.data
        student_id = data.get('student_id')
        student = Student.objects.get(id=student_id)

        # serializer = EnrollmentSerializers(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(student=student, lecture=lecture)
            return Response(serializer.data, status=201)
        

@api_view(['GET', 'PUT', 'DELETE'])
def enrollment_detail(request, id):
    if request.method == 'GET':
        enrollment = Enrollment.objects.get(id=id)
        serializer = EnrollmentSerializers(enrollment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        enrollment = Enrollment.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = EnrollmentSerializers(enrollment, data= data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        enrollment = Enrollment.objects.get(id=id)
        enrollment.delete()
        return Response(status=204) # no content
