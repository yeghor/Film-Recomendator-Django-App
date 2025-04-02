from django.db import models
from django.contrib.auth.models import User
from film_recomendator import settings

class HistorySearchFilm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    movie_id = models.IntegerField()
    
    @property
    def poster_url(self):
        return f"{settings.MEDIA_URL}posters/{self.movie_id}.jpg"


class FilmSearches(models.Model):
    title = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(default=0)
    movie_id = models.IntegerField()

    @property
    def poster_url(self):
        return f"{settings.MEDIA_URL}posters/{self.movie_id}.jpg"