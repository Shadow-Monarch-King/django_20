from django.db import models

# Create your models here.
class Anime(models.Model):
    anime_name = models.CharField(max_length = 100)
    anime_episodes = models.IntegerField()