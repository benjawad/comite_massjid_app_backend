from rest_framework import serializers
from .models import Branch, Cellule, PVReunion


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("id", "name", "description", "image")


class CelluleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellule
        fields = '__all__'

class PVReunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PVReunion
        fields = '__all__'