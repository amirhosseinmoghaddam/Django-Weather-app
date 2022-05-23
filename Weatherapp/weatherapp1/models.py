from datetime import datetime
from operator import truediv
from django.db import models

class Locations(models.Model):
    location = models.CharField(max_length=1000, primary_key=True)

    def __str__(self):
        return self.location