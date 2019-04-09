from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from src.models.announcement.models import Announcement
from src.models.comments.models import Comment


class ArticleDetail(View):

    def get(self, request, *args, **kwargs):
        ob  = Announcement.objects.get(pk=kwargs['pk'])
        return render(request, 'article/detail.html', {'ob': ob})

    def post(self, request, *args, **kwargs):
        article = Announcement.objects.get(pk=kwargs['pk'])
        comment = Comment(
            user        = request.user.profile,
            article     = article,
            text        = request.POST.get('text')
        )
        comment.save()
        return HttpResponseRedirect(reverse('main:article:article_page', kwargs={'pk': kwargs['pk']}))

#
#
# class ArticleDetail(DetailView):
#     queryset        = Announcement.objects.all()
#     template_name   = 'article/detail.html'
#



class UpdateArticle(UpdateView):
    model                   = Announcement
    fields                  = ['title', 'type', 'description', 'location', 'contact']
    template_name           = 'article/update.html'

    def get_object(self, queryset=None):
        obj = super(UpdateArticle, self).get_object(queryset=queryset)
        if obj.user != self.request.user.profile:
            raise Http404
        return obj



class DeleteArticle(DeleteView):
    model                   = Announcement
    template_name           = 'article/delete.html'
    success_url             = reverse_lazy('main:main_page')


    def get_object(self, queryset=None):
        obj = super(DeleteArticle, self).get_object(queryset=queryset)
        if obj.user != self.request.user.profile:
            raise Http404
        return obj
