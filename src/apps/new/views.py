from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from src.models.announcement.models import Announcement



class CreateNew(LoginRequiredMixin,CreateView):
    template_name   = 'new/index.html'
    model           = Announcement
    fields          = [
        'title',
        'type',
        'location',
        'description',
        'contact'
    ]
    success_url     = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)
