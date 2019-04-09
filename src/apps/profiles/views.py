from django.views import View
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from src.models.profiles.models import Profile



class ProfilesView(ListView):
    model            = Profile
    template_name    = 'profile/index.html'


class ProfileDetail(DetailView):
    queryset                = Profile.objects.all()
    context_object_name     = 'profile'
    template_name           = 'profile/detail.html'



class UpdateProfile(UpdateView):
    model                   = Profile
    fields                  = ['firstname', 'lastname', 'description', 'img']
    template_name           = 'profile/update.html'

    def get_object(self, queryset=None):
        obj = super(UpdateProfile, self).get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404
        return obj
