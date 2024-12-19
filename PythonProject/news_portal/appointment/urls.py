from appointment.views import AppointmentView
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('makeappointment/', AppointmentView.as_view(), name='appointment'),

]