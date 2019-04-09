from django.views import View
from src.forms.login.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('main:main_page'))
        form = LoginForm()
        return render(request, 'login/index.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email       = form.cleaned_data.get('email')
            password    = form.cleaned_data.get('password')
            user        = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:main_page')
            else:
                return redirect('main:login:login_page')
