from django.db import models
from django.http import HttpResponse

# Create your models here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cell = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
