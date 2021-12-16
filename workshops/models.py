from django.db import models


class Workshop(models.Model):
    title = models.CharField('Название', max_length=200)
    organizer_email = models.EmailField("Электронная почта")
