from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Profile
from .forms import UserRegisterForm, \
    UserAuthenticationForm, \
    ProfileUpdateForm, \
    UserUpdateForm, \
    PasswordResetForm, \
    UserSetNewPasswordForm, UserForgotPasswordForm

from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'Users/register.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Успешная регистрация')
        return redirect('blog-home')


class UserForgotPasswordView(PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'Users/password_reset.html'
    email_template_name = 'Users/email/password_reset_mail.html'
    subject_template_name = 'Users/email/password_subject_reset_mail.txt'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'Users/password_reset_confirm.html'
    success_url = reverse_lazy('blog-home')


class UserProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'Users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        context['user'] = self.request.user

        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']

        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)

        messages.success(self.request, f'Profile has been changed')
        return super(UserProfile, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')


class UserAuth(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'Users/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'Успешная авторизация')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog-home')


def logout_user(request):
    logout(request)
    return redirect('login')


class PasswordResetDoneView(DetailView):
    pass