from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime

from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            message=appointment.message,
            from_email='alexph10@mail.ru',
            recipient_list=[]
        )

        return redirect('/')