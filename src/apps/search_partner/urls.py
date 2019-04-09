from django.urls import path
from .views import SearcPartners

app_name = 'search_partner'


urlpatterns = [
    path('', SearcPartners.as_view(), name='search_partner_page'),
]
