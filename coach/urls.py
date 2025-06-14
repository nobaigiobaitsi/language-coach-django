from django.urls import path
from .views import api_test_view

urlpatterns = [
    path('test-api/', api_test_view, name='api_test'),
]
