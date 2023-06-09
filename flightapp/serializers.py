from .models import Flight, Reservation, Passenger
from rest_framework import serializers
import re

# def isFlightNumberValid(data):
#     if(re.match("^[a-zA-Z0-9]*$", data['flightNumber']) == None):
#             raise serializers.ValidationError("Flight number must be alphanumeric")
#     return data


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        # validators = [isFlightNumberValid]
        
    def validate_flightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$", flightNumber) == None):
            raise serializers.ValidationError("Flight number must be alphanumeric")
        return flightNumber
    
    # def validate(self, data):
    #     # Put validation logic here
    #     if(re.match("^[a-zA-Z0-9]*$", data['flightNumber']) == None):
    #         raise serializers.ValidationError("Flight number must be alphanumeric")
    #     return data
     
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
   
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'