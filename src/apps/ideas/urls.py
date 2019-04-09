from django.urls import path
from .views import IdeasView

app_name = 'ideas'


urlpatterns = [
    path('', IdeasView.as_view(), name='ideas_page'),
]
