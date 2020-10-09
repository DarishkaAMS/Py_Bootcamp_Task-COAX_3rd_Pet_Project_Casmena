from django.urls import path, include
from lessons import views

urlpatterns = [
    path("", views.LessonAPIView.as_view(), name="homepage"),
    ]
