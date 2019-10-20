from django.db import models

from datetime import timedelta
from django.utils import timezone
# Create your models here.

def gametimedefault():
    return timezone.now() + timedelta(minutes=10)


class PlayDetail(models.Model):
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    winner = models.CharField(max_length=50,default='Draw')
    timeout_in = models.TimeField(default=gametimedefault)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.winner

