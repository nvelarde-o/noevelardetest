from .models import ShortURL
import requests
from bs4 import BeautifulSoup

def update_titles():
	"""
	Cronjob
	Gets the title from the original url and assigns it to the objects that does not have
	one.
	"""
	no_title_urls = ShortURL.objects.filter(page_title__isnull=True)
	for url in no_title_urls:
		result = requests.get(url.original_url)
		soup = BeautifulSoup(result.text, 'html.parser')
		url.page_title = soup.title.name
		url.save()
