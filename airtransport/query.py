from airtransport.models import *


q = Flights.objects.all().filter(departure_airport__airport_code='FRA', arrival_airport__airport_code='LHR')
a = q[0].aircraft_code
seats = Seats.objects.all().filter(aircraft_code=a)
taken = BoardingPasses.objects.all().filter(flight_id=q[0].flight_id)
passengers = [i.ticket_no.passenger_name for i in taken]
