from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .serializers import StudentSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializers(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id=id)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        student = Student.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = StudentSerializers(student, data=data, partial=True)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=204) # no content
# Create your views here.
