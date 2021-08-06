from django.contrib import admin
from .models import Expert

# Register your models here.


class ExpertAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']


admin.site.register(Expert, ExpertAdmin)

admin.site.site_header = 'Welcome to Lizards Back-end Management System'
admin.site.site_title = 'Welcome to Lizards Back-end Management System'