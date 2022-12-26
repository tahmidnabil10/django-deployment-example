from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfoForm(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)

    #additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank = True)

    def __str__(self):
        return self.user.username
