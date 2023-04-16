from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views
from django.contrib.auth.models import User

from .models import Profile
from .untils import InputMixin


class UserRegisterForm(InputMixin, UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email')


class UserAuthenticationForm(InputMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = all


class UserUpdateForm(InputMixin, forms.ModelForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)