from django.shortcuts import render
from django.db import models
from requests import Response
from rest_framework.views import APIView
# Create your models here.
from lessons.models import Lesson
from serializers.models import LessonSerializer

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")

class LessonAPIView(APIView):

    def get(self, *args, **kwargs):
        instances = Lesson.objects.all()
        ser = LessonSerializer(instances, many=True)

        return Response(data=ser.data)
