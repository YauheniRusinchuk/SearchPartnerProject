from django.db import models
from django.shortcuts import reverse
from src.models.profiles.models import Profile


class Announcement(models.Model):


    FIELDS          = (
        ('SEARCH','Search Partners'),
        ('IDEAS','Ideas'),
        ('JOBS', 'Jobs and side jobs'),
    )

    user            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title           = models.CharField(max_length=255, blank=False)
    type            = models.CharField(max_length=100,choices=FIELDS, blank=False)
    location        = models.CharField(max_length=255, blank=True)
    description     = models.TextField(blank=False)
    create_date     = models.DateTimeField(auto_now_add=True)

    contact         = models.CharField(max_length=255, blank=True)


    class Meta:
        ordering = ['-create_date']



    def __str__(self):
        return f"{self.title}"


    def get_absolute_url(self):
        return reverse('main:article:article_page', kwargs={'pk': self.pk})


    def get_absolute_url_update(self):
        return reverse('main:article:article_update', kwargs={'pk': self.pk})


    def get_absolute_url_delete(self):
        return reverse('main:article:article_delete', kwargs={'pk': self.pk})
