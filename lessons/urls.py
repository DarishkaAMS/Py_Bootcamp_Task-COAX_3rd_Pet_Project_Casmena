from django.urls import path, include
from lessons import views

urlpatterns = [
    # path("", views.LessonAPIView.as_view(), name="homepage"),
    path("homepage", views.homepage, name="homepage"),
    path("user", views.user, name="user"),
    # path("<int:lesson_id>", views.lesson, name="lesson"),
    ]
