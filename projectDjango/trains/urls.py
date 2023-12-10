from django.urls import path
from .views import *

urlpatterns = [
    path('trains', train_view),
    path('', schedule_view),
]
