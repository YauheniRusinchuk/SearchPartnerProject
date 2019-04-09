from django.db import models
from src.models.profiles.models import Profile
from src.models.announcement.models import Announcement

class Comment(models.Model):
    
    user            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article         = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text            = models.TextField(blank=False)
    create_date     = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"comment {self.article.title}"
