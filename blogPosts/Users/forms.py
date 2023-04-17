from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
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


class PasswordResetForm(InputMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email')


class PasswordSetForm(InputMixin, SetPasswordForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)