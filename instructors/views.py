from django.shortcuts import render
from django.http import HttpResponse

from .models import Instructor
from .serializers import InstructorSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def instructor_list(request):
    if request.method == 'GET':
        instructor = Instructor.objects.all()
        serializer = InstructorSerializers(instructor, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = InstructorSerializers(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        

@api_view(['GET', 'PUT', 'DELETE'])
def instructor_detail(request, id):
    if request.method == 'GET':
        instructor = Instructor.objects.get(id=id)
        serializer = InstructorSerializers(Instructor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        Instructor = Instructor.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = InstructorSerializers(Instructor, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        Instructor = Instructor.objects.get(id=id)
        Instructor.delete()
        return Response(status=204) # no content