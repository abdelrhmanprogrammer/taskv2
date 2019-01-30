from django.contrib import admin
from .models import post
# Register your models here.
class modelad(admin.ModelAdmin):
    list_display=['__str__','slug']
    class Meta:
        model = post
admin.site.register(post,modelad)