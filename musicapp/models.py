from django.db import models, migrations
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
	first_name = models.CharField(max_length= 100)
	last_name = models.CharField(max_length= 100)
	age= models.IntegerField()

class Song(models.Model):
	Artiste= models.ForeignKey(Artiste, on_delete = models.CASCADE)
	title= models.CharField(max_length= 100)
	date_released= models.DateTimeField(default= datetime.today)
	likes= models.IntegerField(default = 1)
	artiste_id= models.CharField(max_length= 100)

def __str__(self):
	return self.title

class Lyric(models.Model):
	Song= models.ForeignKey(Song, on_delete = models.CASCADE)
	content= models.CharField(max_length= 400)
	song_id= models.IntegerField(default= 1)

def __str__(self):
	return self.content
