from django.contrib import admin
from app.models import *
# Register your models here.

class Webpagecustomview(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['name']
    list_display_links=['topic_name','url']
    list_per_page=2
    search_fields=['name']
    list_filter=['topic_name','name']

admin.site.register(Topic)
admin.site.register(Webpage,Webpagecustomview)
admin.site.register(Access_records)
