from django.contrib import admin
from .models import *


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'tariff_zone']


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['train_number', 'type', 'carriage_number']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_station', 'end_station', 'start_time', 'end_time', 'pass_station', 'train']
