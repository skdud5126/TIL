from django.db import models

# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=255)
    content = models.TextField()
    is_completed = models.BooleanField()
    created_at = models.DateField()