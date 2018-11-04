from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    concert = models.CharField(max_length=100)
    performance_date = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.concert
