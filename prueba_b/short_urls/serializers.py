from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShortURL
		fields = ['visits', 'page_title']
