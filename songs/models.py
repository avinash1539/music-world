from django.contrib.auth.models import User
from django.db import models

class Songs(models.Model):
    song_id = models.AutoField(primary_key = True)
    song_name =  models.CharField(max_length=2000)
    singer_name = models.CharField(max_length=1000)
    tag = models.CharField(blank=False,max_length=1000)
    image = models.ImageField(blank=False,upload_to='images')
    song = models.FileField(upload_to='song')

    def __str__(self):
        return self.song_name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song_id = models.CharField(max_length=100000, default='')

class History(models.Model):
    hist_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_id = models.CharField(max_length=100000, default='')