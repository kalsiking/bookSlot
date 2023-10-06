from django.db import models
from datetime import datetime, timedelta
from customers.models import Customer

# Create your models here.
class Service(models.Model):
    Service = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    LengthInMinutes = models.IntegerField()
    Charge = models.FloatField()

    def __str__(self):
        return self.Service


class Schedules(models.Model):
    StartTime = models.DateTimeField(max_length=100)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    ServiceTable = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        result = ""
        if self.Customer:
            result += str(self.Customer)
        LengthInMinutes = 60
        if self.ServiceTable:
            LengthInMinutes = self.ServiceTable.LengthInMinutes
        EndTime = self.StartTime + timedelta(minutes=LengthInMinutes)
        result += (
            " "
            + datetime.strftime(self.StartTime, "%x")
            + ", "
            + datetime.strftime(self.StartTime, "%X")
            + " "
            + "  "
            + " to "
            + datetime.strftime(EndTime, "%X")
            + "   "
        )
        if self.ServiceTable:
            result += str(self.ServiceTable)
        return result
