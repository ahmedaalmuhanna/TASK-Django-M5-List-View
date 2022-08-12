from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import ListFlightSerializer, ListBookingSerializer

class BookingListApiView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = ListBookingSerializer
    
    
    
class FlightsListApiView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListFlightSerializer