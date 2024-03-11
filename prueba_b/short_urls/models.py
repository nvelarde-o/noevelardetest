from django.db import models
from django.conf import settings

class ShortURL(models.Model):
	original_url = models.CharField(max_length=1000)
	short_url = models.CharField(max_length=1000, unique=True)
	visits = models.IntegerField(default=0)
	page_title = models.CharField(max_length=1000, null=True, blank=True)

	def get_new_url(self):
		return f'{settings.BASE_URL}{self.short_url}'
