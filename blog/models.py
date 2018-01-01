from django.contrib import admin
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()