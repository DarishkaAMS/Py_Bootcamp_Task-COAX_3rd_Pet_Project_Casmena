from pprint import pprint

from django.db import models
from rest_framework import serializers

# Create your models here.

#TODO Serializer

class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = AuthorSerializer()
    lesson_title = serializers.CharField()
    lesson_descr = serializers.CharField()
