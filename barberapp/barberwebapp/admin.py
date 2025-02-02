from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  User,Barber,Service,Appointment,WorkingHours, Reviews

class WorkingHoursInline(admin.StackedInline):
    model = WorkingHours
    extra = 0  # Ne dodaje prazne forme automatski
    can_delete = True  # Dozvoljava brisanje ako je potrebno


class BarberAdmin(admin.ModelAdmin):
    inlines = [WorkingHoursInline]  # Povezivanje radnog vremena s barberom
    list_display = ('name', 'rating')  # Prikaz imena i ocjene u admin sučelju

admin.site.register(User, UserAdmin)
admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(WorkingHours)
admin.site.register(Reviews)

