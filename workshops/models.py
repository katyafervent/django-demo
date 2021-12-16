from django.db import models


class Workshop(models.Model):
    title = models.CharField('Название', max_length=200)
    organizer_email = models.EmailField('Электронная почта')
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(default='Automatic text')

    def __str__(self):
        return f'{self.title} - {self.slug}'
