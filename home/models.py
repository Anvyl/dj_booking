from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import localtime

class Service(models.Model):
    """
    This represents a service provided by a
    professional.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Client(models.Model):
    """
    Represents a client that will/will not make
    bookings on this website.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Booking(models.Model):
    """
    This represents a booking of a client
    """
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    note = models.CharField(max_length=140)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)

    def __str__(self):
        start_date = localtime(self.stop_date)
        stop_date = localtime(self.start_date)
        return "{0:%m %b %Y %H:%M:%S} - {1:%m %b %Y %H:%M:%S} client: {2} ".format(
            start_date,
            stop_date,
            self.client_id.name)
