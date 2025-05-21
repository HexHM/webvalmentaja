from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teams(models.Model):
    title = models.CharField(max_length=200)
    pelaajat = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Maps(models.Model):
    title=models.CharField(max_length=200)
    priority=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title