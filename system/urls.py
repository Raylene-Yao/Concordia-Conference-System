from django.urls import path
from . import views


urlpatterns = [
    # Configure conference information
    path('conference', views.display_conference, name='display_conference'),
    # Configure event information
    path('event', views.display_event, name='display_event'),
]
