import uuid
from datetime import date
from django.db import models
from django.utils import timezone


# Create your models here.
class Status(models.Model):
    Id = models.IntegerField(primary_key=True, editable=False)
    Code = models.CharField(max_length=10)
    Desc = models.CharField(max_length=10)

    def __str__(self):
        return f'Status {self.Code}'


class Estate(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=10)
    Address = models.CharField(max_length=10)
    Contact = models.CharField(max_length=10)
    StatusID = models.IntegerField
    Created_on = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return f'Estate {self.Name}'


class Room(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RoomNumber = models.CharField(max_length=10)
    RoomDesc = models.CharField(max_length=10)
    EstateID = models.ForeignKey(Estate, on_delete=models.CASCADE)  # ForeignKey to Estate
    StatusID = models.IntegerField()
    Created_on = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return f'Room {self.RoomNumber}'






