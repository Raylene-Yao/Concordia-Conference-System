from django.shortcuts import render
from django.http import HttpResponse
from system.models import Conference, Event
from .filters import EventFilter
from datetime import datetime


# Display conference information
def display_conference(request):
    try:
        conference_list = Conference.objects.all()
        conference_context = {"conferencelist": conference_list}
        # Load Template
        return render(request, "system/conference/conlist.html", conference_context)
    except:
        return HttpResponse("Error: no conference information.")


# Display event information
def display_event(request):
    try:
        event_list = Event.objects.all()
        # Use filter
        event_filter = EventFilter(request.GET, queryset=event_list)
        event_list = event_filter.qs
        event_context = {"eventlist": event_list, "eventfilter": event_filter}
        # Load Template
        return render(request, "system/event/evelist.html", event_context)
    except:
        return HttpResponse("Error: no event information.")


def search_event(request):
    key_word = request.GET.get('q')
    if isinstance(key_word, datetime.date()):
        to_filter = f'event_initial_date={key_word}'
    else:
        to_filter = f"event_room={key_word}"
    try:
        event_list = Event.objects.filter(to_filter)
        # Use filter
        event_filter = EventFilter(request.GET, queryset=event_list)
        event_list = event_filter.qs
        event_context = {"eventlist": event_list, "eventfilter": event_filter}
        # Load Template
        return render(request, "system/event/evelist.html", event_context)
    except:
        return HttpResponse("Error: no event information.")
