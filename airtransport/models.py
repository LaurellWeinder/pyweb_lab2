from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Bookings(models.Model):
    book_ref = models.CharField(max_length=50, primary_key=True)
    book_date = models.DateField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.book_ref}:{self.book_date}'


class Tickets(models.Model):
    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    passenger_id = models.IntegerField()
    passenger_name = models.TextField(max_length=250)
    contact_data = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.passenger_name}, id: {self.passenger_id}, ticket:{self.ticket_no}'

class Airport(models.Model):
    airport_code = models.CharField(max_length=3, primary_key=True)
    airport_name = models.TextField()
    city = models.TextField()
    coordinates = models.TextField()
    timezone = models.FloatField()

    def __str__(self):
        return f'{self.airport_name}({self.airport_code}, {self.city})'

class Aircrafts(models.Model):
    aircraft_code = models.CharField(max_length=10, primary_key=True)
    ac_model = models.TextField()
    ac_range = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.aircraft_code} - {self.ac_model}'

class Flights(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)
    flight_no = models.CharField(max_length=10)
    scheduled_departure = models.TimeField()
    scheduled_arrival = models.TimeField()
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    status = models.CharField(max_length=100)
    aircraft_code = models.ForeignKey(Aircrafts, on_delete=models.CASCADE)
    actual_departure = models.TimeField(default=scheduled_departure)
    actual_arrival = models.TimeField(default=scheduled_arrival)

    def __str__(self):
        return f'Flight {self.flight_no} from {self.departure_airport} to {self.arrival_airport} at {self.scheduled_departure}'


class TicketFlights(models.Model):
    ticket_no = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    fare_conditions = models.TextField()
    fare_amount = models.IntegerField()

    class Meta:
        unique_together = ('ticket_no', 'ticket_no')

    def __str__(self):
        return f'Flight:{self.flight_id}, Ticket: {self.ticket_no}'


class BoardingPasses(models.Model):
    ticket_no = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    boarding_no = models.PositiveIntegerField()
    seat_no = models.CharField(max_length=10)

    class Meta:
        unique_together = ('ticket_no', 'flight_id')

    def __str__(self):
        return f'Flight:{self.flight_id}, Ticket: {self.ticket_no}'



class Seats(models.Model):
    aircraft_code = models.ForeignKey(Aircrafts, on_delete=models.CASCADE)
    seats_no = models.CharField(max_length=10)
    fare_conditions = models.CharField(max_length=100)

    class Meta:
        unique_together = ('aircraft_code', 'seats_no')

    def __str__(self):
        return f'{self.seats_no} at {self.aircraft_code}'