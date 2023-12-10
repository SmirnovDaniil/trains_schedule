from django.http import HttpResponse
from django.shortcuts import render
from .models import Train, Station, Schedule


def train_view(request):
    train_list = []
    for train in Train.objects.order_by('train_number'):
        d = dict()
        d['train_name'] = train.train_number
        d['train_type'] = train.type
        d['carriage_number'] = train.carriage_number
        schedule_list = []
        for schedule in Schedule.objects.filter(train=train):
            schedule_list.append(
                {
                    "schedule": schedule.start_station.station_name + " "
                                + str(schedule.start_time) + " - "
                                + schedule.end_station.station_name + " "
                                + str(schedule.end_time)
                }
            )
        d['count'] = 1 if len(schedule_list) == 0 else len(schedule_list)
        d['schedule_list'] = schedule_list
        train_list.append(d)
    return render(request, "trains/index.html", {'trains': train_list})


def schedule_view(request):
    schedule_list = []
    for schedule in Schedule.objects.order_by('start_time'):
        d = dict()
        d['start_station_name'] = schedule.start_station.station_name
        d['start_station_tariff_zone'] = schedule.start_station.tariff_zone

        d['end_station_name'] = schedule.end_station.station_name
        d['end_station_tariff_zone'] = schedule.end_station.tariff_zone

        d['start_time'] = schedule.start_time
        d['end_time'] = schedule.end_time
        d['train'] = schedule.train.train_number
        d['pass_station'] = schedule.pass_station

        schedule_list.append(d)
    return render(request, "trains/schedule.html", {'schedule_list': schedule_list})
