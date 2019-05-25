from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = 'post'

    title = models.CharField(max_length=140)
    date = models.DateField()
    body = models.TextField()