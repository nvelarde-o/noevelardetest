from django.urls import path
from .views import CreateShortURL, GetTop100URLS

urlpatterns = [
    path('create-short-url/', CreateShortURL.as_view()),
    path('get-top-100-urls/', GetTop100URLS.as_view())
]
