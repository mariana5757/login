from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user
