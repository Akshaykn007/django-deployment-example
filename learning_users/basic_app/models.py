from django.db import models
from django.contrib.auth.models import User
from .validators import file_size
# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y",validators=[file_size])

    def __str__(self):
        return self.caption

class Image(models.Model):
    captionim=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.captionim

class Documents(models.Model):
    captiondoc=models.CharField(max_length=100)
    docs=models.FileField(upload_to="doc/%y")

    def __str__(self):
        return self.captiondoc
