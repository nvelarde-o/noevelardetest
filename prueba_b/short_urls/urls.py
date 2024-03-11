from django.urls import path
from .views import RedirectToOriginalURL

urlpatterns = [
    path('<str:short_url_string>/', RedirectToOriginalURL.as_view()),
]
