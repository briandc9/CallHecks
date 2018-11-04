from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    links = models.DateTimeField(default=timezone.now)
    realname = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.concert
