from django.utils import timezone
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView

from barberapp.settings import LOGOUT_REDIRECT_URL
from .models import User,Barber,Service, Appointment, WorkingHours, Reviews
from .forms import BarberForm, ServiceForm, AppointmentForm, ReviewForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from rest_framework import viewsets
from .serializers import BarberSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'barberwebapp/index.html')


def home(request):
    barbers = Barber.objects.all()
    return render(request, 'barberwebapp/home.html', {'barbers': barbers})

def profile(request):
    return render(request,'barberwebapp/profile.html')

def admin_dashboard(request):
    return render(request,'barberwebapp/admin_dashboard.html')

# Registracija
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Lozinke se ne podudaraju!')
            return redirect('register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Korisničko ime već postoji!')
            return redirect('register.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registracija uspješna! Možete se prijaviti.')
        return redirect('login.html')

    return render(request, 'register.html')

# Prijava
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('barberwebapp:home')
        else:
            messages.error(request, 'Neispravni podaci za prijavu!')

    return render(request, 'login.html')

# Odjava
def logout_view(request):
    LOGOUT_REDIRECT_URL(request)
    return redirect('barberwebapp/login.html')

@login_required
def profile_view(request):
    return render(request, 'barberwebapp/profile.html', {'user': request.user})

class BarberListView(ListView):
    model = Barber
    template_name = 'barber_list.html' 
    context_object_name = 'barberi'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset


class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'usluge'
    paginate_by = 10

    
    def get_queryset(self):
        queryset = super().get_queryset()
        max_price = self.request.GET.get('max_price', None)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'
    context_object_name = 'termini'
    paginate_by = 10

    
    def get_queryset(self):
        queryset = super().get_queryset()
        date_filter = self.request.GET.get('date', None)
        if date_filter:
            queryset = queryset.filter(date=date_filter)
        return queryset
    



class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews_list.html'
    context_object_name = 'recenzije'
    paginate_by = 10

    
    def get_queryset(self):
        queryset = super().get_queryset()
        min_rating = self.request.GET.get('min_rating', None)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        return queryset
    


class BarberDetailView(DetailView):
    model = Barber
    template_name = 'barber_detail.html'
    context_object_name = 'barber'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'
    context_object_name = 'appointment'


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'reviews_detail.html'
    context_object_name = 'review'


def create_barber(request):
    if request.method == 'POST':
        form = BarberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barber_list')
    else:
        form = BarberForm()
    return render(request, 'barberwebapp/create_barber.html', {'form': form})

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'barberwebapp/create_service.html', {'form': form})

def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', pk=pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'barberwebapp/update_service.html', {'form': form})




def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', pk=pk)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'barberwebapp/update_appointment.html', {'form': form})


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_list')
    else:
        form = ReviewForm()
    return render(request, 'barberwebapp/create_review.html', {'form': form})

def update_review(request, pk):
    review = get_object_or_404(Reviews, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'barberwebapp/update_review.html', {'form': form})


def update_barber(request, pk): 
    barber = get_object_or_404(Barber, pk=pk) 
    if request.method == 'POST': 
        form = BarberForm(request.POST, instance=barber) 
        if form.is_valid(): 
            form.save() 
            return redirect('barber_detail', pk=pk) 
    else: 
        form = BarberForm(instance=barber) 
    return render(request, 'barberwebapp/update_barber.html', {'form': form})



class BarberDeleteView(DeleteView):
    model = Barber
    template_name = 'barberwebapp/barber_confirm_delete.html'
    success_url = reverse_lazy('barber_list')

class ServiceDeleteView(DeleteView): 
    model = Service 
    template_name = 'barberwebapp/service_confirm_delete.html' 
    success_url = reverse_lazy('service_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'barberwebapp/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

class ReviewDeleteView(DeleteView):
    model = Reviews
    template_name = 'barberwebapp/review_confirm_delete.html'
    success_url = reverse_lazy('reviews_list')


class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]

@login_required
def my_appointments(request):
    # Dohvati sve termine za prijavljenog korisnika
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'barberwebapp/my_appointments.html', {'appointments': appointments})


@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.created_at = timezone.now() 
            appointment.save()
            return redirect('barberwebapp:my_appointments')
    else:
        form = AppointmentForm()
    
    barbers = Barber.objects.all()
    return render(request, 'barberwebapp/home.html', {'form': form, 'barbers': barbers})


@login_required
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Termin je uspješno otkazan.")
        return redirect('barberwebapp:my_appointments')
    return render(request, 'barberwebapp/cancel_appointment.html', {'appointment': appointment})
