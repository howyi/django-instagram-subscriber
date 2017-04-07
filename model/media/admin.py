from django.contrib import admin
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('date', 'data')

admin.site.register(Media, MediaAdmin)
