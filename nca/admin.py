from django.contrib import admin
from .models import User, Staff, Volunteer, Victim, Location, Activity


# Register your models here.
class LocationList(admin.ModelAdmin):
    list_display = ('name', 'address', 'type', 'city', 'state', 'zipcode')
    list_filter = ('type', 'city')
    search_fields = ('type', 'city')


class ActivityList(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'start_date', 'end_date', 'notes')
    list_filter = ('name', 'type')
    search_fields = ('name', 'type')


admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Volunteer)
admin.site.register(Victim)
admin.site.register(Location, LocationList)
admin.site.register(Activity, ActivityList)
