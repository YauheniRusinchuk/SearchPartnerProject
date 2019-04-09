from django.urls import path
from .views import JobsView



app_name = 'jobs'

urlpatterns = [
    path('', JobsView.as_view(), name='jobs_page'),

]
