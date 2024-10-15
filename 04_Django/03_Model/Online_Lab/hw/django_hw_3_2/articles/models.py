from django.db import models

# Create your models here.
class Articel(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

    