from django.urls import path
from .views import CreateNew

app_name = 'new'


urlpatterns = [
    path('', CreateNew.as_view(), name='new_page'),
]
