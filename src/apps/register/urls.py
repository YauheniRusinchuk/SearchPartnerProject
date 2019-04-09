from django.urls import path
from .views import Register

app_name = 'register'


urlpatterns = [
    path('', Register.as_view(), name='register_page'),
]
