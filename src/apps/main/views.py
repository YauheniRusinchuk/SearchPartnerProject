from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from src.models.announcement.models import Announcement

# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         all = Announcement.objects.all()
#         return render(request, 'main/index.html', {})


class MainView(ListView):
    queryset        = Announcement.objects.all()
    template_name   = 'main/index.html'
    
