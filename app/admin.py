from django.contrib import admin
from app.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'phone', 'message']
admin.site.register(Contact,ContactAdmin)

