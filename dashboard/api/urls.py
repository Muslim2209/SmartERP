from django.urls import path

from dashboard.views import home

app_name = 'api_dashboard'

urlpatterns = [
    path('', home, name='dashboard'),
]
