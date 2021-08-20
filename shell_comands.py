# flake8: noqa
from workshops.models import *
from django.db import connection, reset_queries

new_a = Address(city="Paris", street="Some", building="5")
#change field
new_a.save()

first_address = Address.objects.get(pk=1)
first_address.location
new_a.location # through error

# show model fields
for i in Workshop._meta.get_fields():
    print(i)

# filters
y_2021 = Workshop.objects.filter(date__year=2021)
m_11 = Workshop.objects.filter(date__month=11)

#Select realted https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.select_related
# know in advance that I'm going use locations in a view
w_all = Workshop.objects.all()
[w.location.name for w in w_all]
len(connection.queries)
for c in connection.queries:
    print(c)
reset_queries()
w_all_with_select = Workshop.objects.select_related('location').all()
[w.location.name for w in w_all_with_select]

# set of objects
for workshop in Workshop.objects.all():
    workshop.participants.all()
# here we know that we will operate with participants in advance
for workshop in Workshop.objects.prefetch_related('participants').all():
    workshop.participants.all()