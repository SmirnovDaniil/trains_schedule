import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectDjango.settings')
django.setup()
from trains.models import *

Train.objects.all().delete()
Station.objects.all().delete()
Schedule.objects.all().delete()

train_data = [
    {"train_number": "6352", "type": "Стандарт", "carriage_number": 6},
    {"train_number": "7234", "type": "Иволга", "carriage_number": 5},
    {"train_number": "7046", "type": "Фирменный экспресс", "carriage_number": 7},
]

train_list = []
for t in train_data:
    train = Train(**t)
    train_list.append(train)
    train.save()

station_data = [
    {'station_name': 'Москва (Савёловский вокзал)', 'tariff_zone': 'Центральная'},
    {'station_name': 'Одинцово', 'tariff_zone': 'Пригород'},
    {'station_name': 'Савёлово', 'tariff_zone': 'Дальная'},
    {'station_name': 'Лобня', 'tariff_zone': 'Пригород'},
    {'station_name': 'Дубна', 'tariff_zone': 'Дальная'},
]

station_list = []
for s in station_data:
    station = Station(**s)
    station_list.append(station)
    station.save()


schedule_data = [
    {"start_station": station_list[0], "end_station": station_list[2], "start_time": datetime.time(13, 46, 0),
     "end_time": datetime.time(16, 25, 0), "train": train_list[0]},
    {"start_station": station_list[2], "end_station": station_list[0], "start_time": datetime.time(17, 33, 0),
     "end_time": datetime.time(21, 10, 0), "pass_station": "Долгопрудная Новодачная", "train": train_list[0]},
    {"start_station": station_list[1], "end_station": station_list[3], "start_time": datetime.time(13, 56, 0),
     "end_time": datetime.time(14, 43, 0), "train": train_list[1]}
]

for sch in schedule_data:
    schedule = Schedule(**sch)
    schedule.save()
