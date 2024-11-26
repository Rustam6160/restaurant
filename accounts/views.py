
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, EditProfileForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User


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

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You\'re logged in')
            return redirect('profile')
        else:
            messages.error(request, 'Error logging in')
            return redirect('login')



class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('home')  # Перенаправление после успешного сохранения

    def get_object(self, queryset=None):
        # Возвращаем текущего пользователя
        return self.request.user

class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = User.objects.get(id=request.user.id)
            return render(request, 'accounts/profile.html', context={'current_user': current_user})
        else:
            return render(request, 'accounts/profile.html')