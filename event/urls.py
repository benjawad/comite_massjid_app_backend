from django.urls import path
from .views import EventList, EventDetail, RateEvent, ContributeToEvent, ShareEvent, HomeEventList   

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/home/', HomeEventList.as_view(), name='home-event-list'),  
    path('events/<int:event_id>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_id>/rate/', RateEvent.as_view(), name='rate-event'),
    path('events/<int:event_id>/contribute/', ContributeToEvent.as_view(), name='contribute'),
    path('events/<int:event_id>/share/', ShareEvent.as_view(), name='share-event'),
]