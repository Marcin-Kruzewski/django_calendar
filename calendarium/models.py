from __future__ import unicode_literals
# import datetime
from django.db import models


class User(models.Model):
    user_login = models.TextField(max_length=35)
    user_password = models.TextField(max_length=100)
    user_name = models.TextField(max_length=50)
    user_cell_nr = models.TextField(max_length=15)
    user_mail = models.TextField(max_length=50)

    def __str__(self):
        return self.user_login


class Host(models.Model):
    host_login = models.TextField(max_length=35)
    host_password = models.TextField(max_length=100)
    host_name = models.TextField(max_length=50)
    host_cell_nr = models.TextField(max_length=15)
    host_mail = models.TextField(max_length=50)

    def __str__(self):
        return self.host_login


class Appointment(models.Model):
    appointment_date = models.DateTimeField()
    appointment_time = models.TimeField()
    appointment_text = models.TextField(max_length=200)
    appointment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_host = models.ForeignKey(Host, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_text
