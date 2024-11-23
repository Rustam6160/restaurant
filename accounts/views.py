
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, EditProfileForm


class RegisterUserView(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You\'re now registered')
            return redirect('home')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

class LoginUserView(View):
    def get(self, request):
        return render(request, 'accounts/login.html', {})



def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/')  # перенаправить на страницу профиля
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
