from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from decimal import Decimal, InvalidOperation
import random

class EventList(generics.ListAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class HomeEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all().order_by('-date')[:5]
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:5]

class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'event_id'

class RateEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, event_id=event_id)
        try:
            rating = int(request.data.get('rating'))
            if rating < 1 or rating > 5:
                raise ValueError
        except (TypeError, ValueError):
            return Response({'message': 'Invalid rating (1-5 required)'}, 
                          status=status.HTTP_400_BAD_REQUEST)

        event.update_rating(rating)
        return Response({'message': 'Rating updated successfully', 'new_rating': event.rating},
                      status=status.HTTP_200_OK)

class ContributeToEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, event_id=event_id)
        try:
            amount = Decimal(request.data.get('amount'))
            if amount <= 0:
                raise ValueError
        except (InvalidOperation, ValueError):
            return Response({'message': 'Invalid contribution amount'}, 
                          status=status.HTTP_400_BAD_REQUEST)

        event.total_donations += amount
        event.save()
        return Response({'message': 'Contribution successful', 
                       'new_total': event.total_donations},
                      status=status.HTTP_200_OK)

class ShareEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, event_id=event_id)
        share_message = f"Check out this event: {event.name} on {event.date}"
        return Response({'message': 'Event shared successfully', 'share_text': share_message},
                      status=status.HTTP_200_OK)
