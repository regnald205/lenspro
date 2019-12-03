from django.contrib import admin
from .models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display=('id','Event_title','Event_date')
    list_display_links=('Event_title','Event_date')
    list_filter=('Event_title','Event_date')
    search_fields=('Event_title','Event_date')
    list_per_page=25


admin.site.register(Upload,UploadAdmin)

