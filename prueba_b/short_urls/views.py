from django.shortcuts import redirect
from django.views import View
from .models import ShortURL

class RedirectToOriginalURL(View):
	def get(self, request, short_url_string):
		"""
		Gets the original URL from the short URL and
		redirects to the original site.
		Throws a 404 response if the original URL doesn't exist.
		"""
		try:
			short_url_obj = ShortURL.objects.get(short_url=short_url_string)
			short_url_obj.visits += 1
			short_url_obj.save()
			return redirect(short_url_obj.original_url)
		except ShortURL.DoesNotExist:
			raise Http404("URL does not exist")
