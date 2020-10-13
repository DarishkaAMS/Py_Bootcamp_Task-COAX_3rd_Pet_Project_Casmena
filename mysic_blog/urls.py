from django.urls import path, include
# from mysic_blog import views -without class
from mysic_blog.views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, like_view, LessonAPIView, AddCategoryView, category_view

# HomeAPIView


urlpatterns = [
    # path('', views.home, name="home") #without class
    path('', HomeView.as_view(), name='home'),
    # path('', HomeAPIView(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', category_view, name="category"),

    path('like/<int:pk>', like_view, name='like_post'),

    path('sergi/', LessonAPIView.as_view(), name='sergi'),

]
