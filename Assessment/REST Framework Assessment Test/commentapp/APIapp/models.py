from django.db import models
from datetime import datetime

# Create your models here.
class commentInfo(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    comment=models.TextField()