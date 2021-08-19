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


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.OneToOneField(Address,
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    class Meta:
        default_related_name = 'location'

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.lastname


class Workshop(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 related_name='location',
                                 blank=False,
                                 null=True)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'
