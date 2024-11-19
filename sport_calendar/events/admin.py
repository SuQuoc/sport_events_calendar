from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Team)
admin.site.register(Sport)
admin.site.register(Country)