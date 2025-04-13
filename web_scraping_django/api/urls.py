from django.urls import path
from .views import ScrapeView

urlpatterns = [
    path('scrape/', ScrapeView.as_view(), name='scrape'),
]
