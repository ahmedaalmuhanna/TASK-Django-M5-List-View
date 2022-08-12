from django.contrib import admin
from .models import Flight, Booking
# Register your models here.
@admin.register(Flight) 
# @admin.register(Booking)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id' , 'destination','time','price')
# class BookingAdmin(admin.ModelAdmin):
#list_display = ('bookings_destination','bookings_time','bookings_price' )
