from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  User,Barber,Service,Appointment,WorkingHours, Reviews

class WorkingHoursInline(admin.StackedInline):
    model = WorkingHours
    extra = 0  
    can_delete = True  


class BarberAdmin(admin.ModelAdmin):
    inlines = [WorkingHoursInline]  
    list_display = ('name', 'rating')  

admin.site.register(User, UserAdmin)
admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(WorkingHours)
admin.site.register(Reviews)

