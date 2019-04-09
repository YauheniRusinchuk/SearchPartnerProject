from django.views.generic import ListView, DetailView
from src.models.announcement.models import Announcement


class IdeasView(ListView):
    queryset        = Announcement.objects.filter(type="IDEAS")
    template_name   = 'ideas/index.html'
