from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.forms import RegisterUserForm, LoginUserForm

logger = logging.getLogger('TEST_LOGGER_NAME')


def index(request):
    logger.info("Загрузка страницы 'Главная'")
    return render(request, 'main/index.html')

def admin(request):
    logger.info("Загрузка страницы 'Админ'")
    return redirect('admin')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')