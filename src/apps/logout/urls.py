from django.urls import path
from .views import logout_view

app_name = 'logout'

urlpatterns = [
    path('', logout_view, name='logout_page'),
]
