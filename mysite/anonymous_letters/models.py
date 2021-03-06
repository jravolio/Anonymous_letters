from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Letter(models.Model):
    title = models.CharField(max_length=200, null = True)
    text = models.TextField(null=True)
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

