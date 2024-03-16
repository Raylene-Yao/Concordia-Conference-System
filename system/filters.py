import django_filters
from django_filters import DateFilter

from .models import *


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = '__all__'
