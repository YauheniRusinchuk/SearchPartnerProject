from django.views.generic import ListView
from src.models.announcement.models import Announcement

class JobsView(ListView):
    queryset        = Announcement.objects.filter(type="JOBS")
    template_name   = 'jobs/index.html'
