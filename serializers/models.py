from pprint import pprint

from django.db import models
from rest_framework import serializers

# Create your models here.


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = AuthorSerializer()
    lesson_title = serializers.CharField()
    lesson_descr = serializers.CharField()

    def test_serializer(self):
        ser=LessonSerializer(instance=self.lesson_title)
        pprint(ser.data)