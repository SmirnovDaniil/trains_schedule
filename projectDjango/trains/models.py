from django.db import models


class Train(models.Model):
    train_number = models.CharField(max_length=100, verbose_name='Номер поезда')
    type = models.CharField(max_length=100, verbose_name='Тип поезда')
    carriage_number = models.IntegerField(verbose_name='Число вагонов')

    def __str__(self):
        return self.train_number

    class Meta:
        verbose_name_plural = 'Поезда'
        verbose_name = 'Поезд'
        ordering = ['train_number']


class Station(models.Model):
    station_name = models.CharField(max_length=100, verbose_name='Название станции')
    tariff_zone = models.CharField(max_length=100, verbose_name='Тарифная зона')

    def __str__(self):
        return self.station_name

    class Meta:
        verbose_name_plural = 'Станция'
        verbose_name = 'Станции'
        ordering = ['station_name']


class Schedule(models.Model):
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                      related_name='schedule_start_station', verbose_name='Станция начала маршрута')

    end_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                    related_name='schedule_end_station', verbose_name='Станция окончания маршрута')

    start_time = models.TimeField(verbose_name='Время отправления')
    end_time = models.TimeField(verbose_name='Время прибытия')
    pass_station = models.CharField(max_length=1000, verbose_name='Станции без остановки')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='Поезд')

    def __str__(self):
        return self.start_station.name + '-' + self.end_station.name

    class Meta:
        verbose_name_plural = 'Расписание'
        verbose_name = 'Расписание'
        ordering = ['start_time']