from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)


class DeliveryTime(models.Model):
    hours = models.CharField(max_length=255, unique=True)


class StorageCondition(models.Model):
    condition = models.CharField(max_length=255, unique=True)


class TransportAvailability(models.Model):
    availability = models.CharField(max_length=255, unique=True)


class Transporter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE)
    storage_condition = models.ForeignKey(StorageCondition, on_delete=models.CASCADE)
    route_availability = models.ForeignKey(TransportAvailability, related_name='route', on_delete=models.CASCADE)
    train_availability = models.ForeignKey(TransportAvailability, related_name='train', on_delete=models.CASCADE)
    sea_availability = models.ForeignKey(TransportAvailability, related_name='sea', on_delete=models.CASCADE)
    air_availability = models.ForeignKey(TransportAvailability, related_name='air', on_delete=models.CASCADE)
    transport_capacity = models.IntegerField()
    vehicle_types = models.CharField(max_length=255)
    itinerary = models.CharField(max_length=255)
    transporter_name = models.CharField(max_length=255)
    delivery_states = models.CharField(max_length=255)
    source = models.CharField(max_length=255)


class Cargo(models.Model):
    transporter = models.ForeignKey(Transporter, on_delete=models.CASCADE)
    cargo_number = models.CharField(max_length=255)
    progress = models.CharField(max_length=255)
    delivery_deadline = models.DateField()
    delay = models.BooleanField(default=False)
    source = models.CharField(max_length=255)
