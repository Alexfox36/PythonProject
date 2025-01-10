from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from datetime import datetime
from django.core.cache import cache

from pyexpat.errors import messages
from rest_framework.response import Response
from unicodedata import category

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions


from .models import *

from .forms import PostForm
from .models import Post, Categories, Author, Comment
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin

from appointment.tasks import send_m

from .serializers import AuthorSerializer, CategoriesSerializer, UserSerializer, CommentSerializer, PostSerializer


class BaseView(TemplateView):
    template_name = 'base.html'


class PostsList(ListView):
    model = Post
    ordering = 'post_date_time'
    template_name = 'news.html'
    context_object_name = 'posts_list'
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now(datetime. UTC)
        context['filterset'] = self.filterset
        return context



class PostsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'single_post'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        send_m.delay()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    form_class = PostForm
    model = Post
    template_name = 'search.html'
    context_object_name = 'post_search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class CategoryList(PostsList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Categories, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-post_date_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Categories.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'Вы подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category':category, 'message':message })



class AuthorViewset(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer
   def list(self, request, format=None):
       return Response([])

   def destroy(self, request, pk, format=None):
       instance = self.get_object()
       instance.is_active = False
       instance.save()
       return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriesViewset(viewsets.ModelViewSet):
   queryset = Categories.objects.all()
   serializer_class = CategoriesSerializer

class UserViewset(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class CommentViewset(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


