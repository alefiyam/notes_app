from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Notes(models.Model):
    # title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.text