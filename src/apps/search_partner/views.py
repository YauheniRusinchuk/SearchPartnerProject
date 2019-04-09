from django.views import View
from django.views.generic import ListView
from django.shortcuts import render
from src.models.announcement.models import Announcement

# 
# class SearcPartners(View):
#
#     def get(self, request, *args, **kwargs):
#         sp = Announcement.objects.filter(type='SEARCH')
#         print(sp)
#         return render(request, 'partners/index.html', {})
#


class SearcPartners(ListView):
    queryset        = Announcement.objects.filter(type="SEARCH")
    template_name   = 'partners/index.html'
