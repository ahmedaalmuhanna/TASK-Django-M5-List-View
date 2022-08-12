from rest_framework import serializers
from .models import Flight,Booking

class ListFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        # fields = ['id' , 'destination','time','price']
        
class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        # fields = ['id','flight' , 'date']