from django.db import models
from home.models import post
# Create your models here.
class cat(models.Model):
    cat = models.CharField(max_length=10)
    posts = models.ManyToManyField(post,blank=True)
    def __str__(self):
        return self.cat