from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.OneToOneField('Address',
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    def __str__(self):
        return f'{self.name} ({self.address})'
