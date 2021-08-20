from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)

    @property
    def address(self):
        return f'{self.city} {self.street} {self.building}'

    def __str__(self):
        return self.address
