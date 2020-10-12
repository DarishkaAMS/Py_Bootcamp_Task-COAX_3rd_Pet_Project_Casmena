from django.urls import path, include
# from mysic_blog import views -without class
from mysic_blog.views import HomeView, ArticleDetailView

urlpatterns = [
    # path('', views.home, name="home") - without class
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]
