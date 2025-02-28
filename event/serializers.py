from rest_framework import serializers
from .models import Event
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(read_only=True)
    is_past = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_details(self, obj):
        return obj.get_details()

    def get_is_past(self, obj):
        return obj.date < timezone.now().date()