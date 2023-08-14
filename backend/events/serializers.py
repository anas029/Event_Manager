from rest_framework import serializers
from .models import Event, Venue
class VenueSerializer(serializers.Serializer):
    class Meta:
        model = Venue
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    # venue = VenueSerializer()  # Nested serializer
    # organizer = serializers.StringRelatedField()  # Display organizer's username
    # participants = serializers.StringRelatedField(many=True)  # Display participants' username

    class Meta:
        model = Event
        fields = '__all__'