from django.contrib import admin
from .models import Workshop
from .models import Location
from .models import Participant
from .models import Address

admin.site.register(Workshop)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Address)
