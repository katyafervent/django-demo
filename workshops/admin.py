from django.contrib import admin

from .models import Address, Location, Participant, Workshop


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(Participant)
