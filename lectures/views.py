from django.shortcuts import render
from django.http import HttpResponse

from .models import Lecture, Instructor
from .serializers import LectureSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from instructors.serializers import Instructor

# Create your views here.

@api_view(['GET', 'POST'])
def lecture_list(request):
    if request.method == 'GET':
        lectures = Lecture.objects.all()
        serializer = LectureSerializers(lectures, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # instructor = Instructor.objects.get(id=id)
        data = request.data
        instructor_id = data.get('instructor_id')
        instructor = Instructor.objects.get(id=instructor_id)

        serializer = LectureSerializers(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(instructor=instructor)
            return Response(serializer.data, status=201)
        

@api_view(['GET', 'PUT', 'DELETE'])
def lecture_detail(request, id):
    if request.method == 'GET':
        lecture = Lecture.objects.get(id=id)
        serializer = LectureSerializers(lecture)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        lecture = Lecture.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = LectureSerializers(lecture, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = Lecture.objects.get(id=id)
        article.delete()
        return Response(status=204) # no content