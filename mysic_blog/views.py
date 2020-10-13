from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView

from mysic_blog.models import Post
from mysic_blog.forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mysic_blog.serializer import PostSerializer
# Create your views here.


class HomeView(ListView): #TRUE ONE -> TO HomeAPIView
    model = Post
    template_name = 'home.html'
    # ordering = ['-post_date']
    ordering = ['-id']


class LessonAPIView(APIView):
    def get(self, *args, **kwargs):
        instances = Post.objects.all()
        ser = PostSerializer(instances, many=True)
        return Response(data=ser.data)


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        obj = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = obj.total_likes()

        liked = False
        if obj.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    # return Response('API BASE POINT', safe=False)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
