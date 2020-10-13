from django.urls import path, include
from members.views import UserRegisterView, UserEditView, ShowProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
]
