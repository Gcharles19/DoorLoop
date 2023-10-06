from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Status)
# admin.site.register(Room)
# admin.site.register(Estate)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['Code','Desc']

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['Name','Address','Contact','Created_on']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['RoomNumber', 'RoomDesc','EstateID', 'Created_on']
    list_filter = ['EstateID']