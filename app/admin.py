from django.contrib import admin
from app.models import *
# Register your models here.
class customisedTopic(admin.ModelAdmin):
    list_display=['topic_name']
 
class customisedWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['url']
    list_editable=['name']
    search_fields=('name',)
    list_filter=('name',)
    list_per_page=1

class customisedAccessRecord(admin.ModelAdmin):
    list_display=['name','date','author']
    list_display_links=['author']
    list_editable=['name']
    search_fields=('name',)
    list_filter=('name',)
    list_per_page=1

admin.site.register(Topic,customisedTopic)

admin.site.register(Webpage,customisedWebpage)

admin.site.register(AccessRecord,customisedAccessRecord)