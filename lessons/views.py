from django.shortcuts import render
from django.db import models
from requests import Response
from rest_framework.views import APIView
# Create your models here.
from lessons.models import Lesson
# from serializers.models import LessonSerializer

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def user(request):
    return render(request, "user.html")


# def lesson(request, lesson_id):
#     lesson = Lesson.objects.get(pk=lesson_id)
#     return render(request, "lesson.html", {
#         "author": lesson.author,
#         "lesson_title": lesson.lesson_title,
#         "lesson_descr": lesson.lesson_descr
#     })

# class LessonAPIView(APIView):
#
#     def get(self, *args, **kwargs):
#         instances = Lesson.objects.all()
#         ser = LessonSerializer(instances, many=True)
#
#         return Response(data=ser.data)
#     def post(self, *args, **kwargs):
#         ser = LessonSerializer(data=self.request.data)
#         ser.is_valid(raise_exception=True)
#         ser.save()
#         return Response(data=ser.data, status=status.HTTP_201_CREATED)
