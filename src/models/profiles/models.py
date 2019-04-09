from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
import os
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname   = models.CharField(max_length=100, blank=False)
    lastname    = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    img         = models.ImageField(upload_to='img_profile/', blank=True)


    def __str__(self):
        return f"profile  {self.user}"

    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def name(self):
        return f"{self.firstname}{self.lastname}"

    def get_absolute_url(self):
        return reverse('main:profiles:profile_detail', kwargs={'name': self.name(), 'pk': self.pk})

    def get_absolute_url_update(self):
        return reverse('main:profiles:profile_update', kwargs={'name': self.name(), 'pk': self.pk})




def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    if not instance.img:
         return False
    old_file = sender.objects.get(user=instance.user).img or None

    if old_file:
        if not old_file == instance.img:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)


pre_save.connect(pre_save_profile_receiver, sender=Profile)
