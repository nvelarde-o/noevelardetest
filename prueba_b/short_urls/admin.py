from django.contrib import admin
from .models import ShortURL

class ShortURLAdmin(admin.ModelAdmin):
	list_display = ["original_url", "short_url", "visits", "page_title"]

admin.site.register(ShortURL, ShortURLAdmin)
