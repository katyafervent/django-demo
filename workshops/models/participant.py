from django.db import models


class Participant(models.Model):
    email = models.EmailField(unique=True)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.lastname
