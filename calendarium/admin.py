from django.contrib import admin
from .models import Appointment, Host, User


class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ['appointment_date', 'appointment_user', 'appointment_host']
    search_fields = ['appointment_text']


class UserAdmin(admin.ModelAdmin):
    search_fields = ['user_name']


class HostAdmin(admin.ModelAdmin):
    search_fields = ['host_name']

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(User, UserAdmin)
