from django.db import models
from django.db.models import Q
import random ; import os
from django.db.models.signals import pre_save , m2m_changed
from .utils import unique_slug_generator
# Create your models here.
#image extension
def get_username_ext(filepath):
    basename= os.path.basename(filepath)
    name,ext = os.path.splitext(basename)
    return name , ext
def img_path(instance,filename):
    new_filename= random.randint(0,15144)
    name , ext  = get_username_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return 'postsimgs/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename=final_filename)
#post manager
class qwery(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    def featured(self):
        return self.filter(active=True,featured=True)
    def search(self,query):
        if query is None :
            return self.filter(active=True)
        else:
            lookups = Q(title__icontains=query)|Q(title__iexact=query)|Q(describtion__icontains=query)|Q(slug__iexact=query)|Q(cat__cat__icontains=query)|Q(cat__cat__iexact=query)
        return self.filter(lookups)
class postsmanager(models.Manager):
    def get_queryset(self):
        return qwery(self.model,using=self._db)
    def search(self,query):
        return self.get_queryset().active().search(query)
    def active(self):
        return self.get_queryset().active()
    def featured(self):
        return self.get_queryset().active().featured()
    def get_by_id(self,id):
        qs = self.filter(id=id)
        if qs.count() :
            qs.first()
        return None ,qs
class post(models.Model):
    title = models.CharField(max_length=10)
    describtion = models.TextField()
    img = models.FileField(upload_to=img_path,blank=True)
    slug = models.SlugField(unique=True,blank=True)
    files = models.FileField(upload_to=img_path,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=True)
    featured= models.BooleanField(default=False)
    objects = postsmanager()
    def __str__(self):
        return self.title


def pre_save_receiver(instance,sender,*args,**kwargs):
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)
pre_save.connect(pre_save_receiver,sender=post)