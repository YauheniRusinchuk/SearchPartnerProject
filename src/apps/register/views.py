from django.views import View
from django.shortcuts import render, redirect
from src.forms.register.forms import RegisterForm
from django.contrib.auth import get_user_model
from src.models.profiles.models import Profile

User = get_user_model()



class Register(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.user.is_authenticated:
            return redirect('main:main_page')
        return render(request, 'register/index.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        print("RESULT : ", request.POST)
        qs = User.objects.filter(email=request.POST.get('email'))
        if qs.exists():
            return redirect('main:register:register_page')
        user = User(email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        try:
            user.save()
        except Exception:
            raise ValueError("Error ....")
        profile = Profile(user=user, firstname=request.POST.get('firstname'),
                            lastname=request.POST.get('lastname'),
                            description=request.POST.get('description'),
                            img= None,
                        )
        profile.save()

        return redirect('main:main_page')
