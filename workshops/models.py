from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    @property
    def address(self):
        return f'{self.city} {self.street} {self.building}'

    def __str__(self):
        return self.address


class Location(models.Model):
    name = models.CharField('Место проведения', max_length=200)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='Место проведения',
    )

    class Meta:
        default_related_name = 'location'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField('Электронная почта', unique=True)
    username = models.CharField('Никнейм', max_length=100)

    def __str__(self):
        return self.username


class Workshop(models.Model):
    title = models.CharField('Название', max_length=200)
    organizer_email = models.EmailField('Электронная почта')
    slug = models.SlugField('Текстовый идентификатор', unique=True)
    date = models.DateField('Дата проведения', auto_now_add=True)
    description = models.TextField(default='Automatic text')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    class Meta:
        default_related_name = 'workshops'

    def __str__(self):
        return f'{self.title} - {self.slug}'
