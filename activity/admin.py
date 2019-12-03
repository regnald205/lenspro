from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display=('title','venue_name','place','Event_date','id')
    list_display_links=('title','id','venue_name','place')
    list_filter=('title','Event_date')
    search_fields=('title','Event_date','place','venue_name')
    list_per_page=25

admin.site.register(Activity, ActivityAdmin)




