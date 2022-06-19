from datetime import datetime
from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text =  models.CharField(max_length=1000000000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    def __str__(self):
        return self.author
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)

   


