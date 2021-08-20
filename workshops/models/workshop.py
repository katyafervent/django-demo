from django.db import models


class Workshop(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.ForeignKey('Location',
                                 on_delete=models.CASCADE,
                                 related_name='location',
                                 blank=False,
                                 null=True)
    participants = models.ManyToManyField('Participant',
                                          blank=True,
                                          null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'
