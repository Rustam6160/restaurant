from django.urls import path
from .views import *


urlpatterns = [
    path('', Reservation.as_view(), name='reservation'),

]