from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from short_urls.models import ShortURL
from short_urls.serializers import ShortURLSerializer

import random
import string

# Create your views here.
class CreateShortURL(APIView):
	def get_random_string(self):
		"""
		Creates a random string of length 10
		"""
		letters = string.ascii_lowercase
		random_str = ''.join(random.choice(letters) for i in range(10))
		return random_str

	def post(self, request):
		"""
		Creates a shorter URL from the original URL and returns it.
		Returns a 500 status error if there is no original URL provided.
		"""
		original_url = request.POST.get('url', None)
		try:
			if not original_url:
				raise Exception
			
			random_str = self.get_random_string()
			
			# If the random generated string already exists, create another one.
			while ShortURL.objects.filter(short_url=random_str).exists():
				random_str = self.get_random_string()

			new_url_obj = ShortURL(
				original_url=original_url,
				short_url=random_str
			)
			new_url_obj.save()
			
			return Response({'short_url': f'{new_url_obj.get_new_url()}'}, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({'status': f'{e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTop100URLS(APIView):
	def get(self, request):
		"""
		Gets the top 100 most visited URL's
		Orders the url objects by most visits and performs a slice to last 100.
		Returns a Json object with the serialized data.
		"""
		top_urls = ShortURL.objects.all().order_by('-visits')[:100]
		serializer = ShortURLSerializer(top_urls, many=True)
		return JsonResponse(serializer.data, safe=False)
