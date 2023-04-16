from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy

from Users.untils import InputMixin
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post_form.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'Blog/post_delete.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('blog-home')

    def form_valid(self, form):
        messages.success(self.request, f'Post has been deleted')
        return super().form_valid(form)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'Blog/post_create.html'
    form_class = PostForm
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'Blog/post_update.html'
    form_class = PostForm
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование поста: '
        return context

    def form_valid(self, form):
        with transaction.atomic():
            if form.is_valid():
                form.save()

        messages.success(self.request, f'Post has been changed')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False