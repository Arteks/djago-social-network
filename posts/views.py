from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'

class PostDetail(DetailView):
    model = Post

class PostCreation(CreateView):
    model = Post
    success_url = reverse_lazy('posts:list')
    fields = ['title', 'body', 'autor']

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('posts:list')
    fields = ['title', 'body', 'autor']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')
