from django.urls import path, include
from members.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
