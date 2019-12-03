from django.contrib import admin
from .models import Contact_client

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','contact_date')
    list_display_links=('name','email','phone','contact_date')
    search_fields=('name','email')
    list_per_page=25


admin.site.register(Contact_client,ContactAdmin)
