
from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

class News(models.Model):
    headline = models.CharField(max_length = 250)
    text = models.TextField()
    author = models.CharField(max_length = 120)
    datemonth = models.CharField(max_length=50)
    def __str__(self):
        return self.headline
    objects = models.Manager

class userProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    last_scrape = models.DateTimeField(auto_now_add=True,null =True)
    def __str__(self):
        return "{}-{}".format(self.user,self.last_scrape)
    objects = models.Manager