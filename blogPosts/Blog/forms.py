from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.forms import ModelForm

from Users.untils import InputMixin
from .models import Post


class PostForm(InputMixin, ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')