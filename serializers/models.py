# from pprint import pprint
#
# from django.db import models
# from rest_framework import serializers
#
# # Create your models here.
#
# #TODO Serializer
# from lessons.models import Lesson
#
#
# class ValidaionError(object):
#     pass
#
#
# class LessonSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     # author = AuthorSerializer()
#     lesson_title = serializers.CharField()
#     lesson_descr = serializers.CharField()
#
#     # def validate_lesson(self, value):
#     #     id_ = value.get('id')
#     #     try:
#     #         author = Lesson.objects.get(id=id)
#     #         if author.name == "Somebody":
#     #             raise ValidaionError("f")
