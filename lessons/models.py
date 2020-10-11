from django.db import models

from authentication.models import USER


class Lesson(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=25)
    lesson_descr = models.CharField(max_length=255)
    # video = models.FileField(upload_to='images/', blank=True, null=True) #!!!!

    class Meta:
        db_table = "lessons"

    def __str__(self):
        return f"{self.lesson} run by {self.author} ({self.stuff} members)"  # {self.id}:
