from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import User,Barber,Service, Appointment, WorkingHours, Reviews
from .forms import BarberForm, ServiceForm, AppointmentForm, ReviewForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.


def index(request):
    return render(request, 'barberwebapp/index.html')


def home(request):
    barbers = Barber.objects.all()
    return render(request, 'barberwebapp/home.html', {'barbers': barbers})


def profile(request):
    return render(request,'barberwebapp/profile.html')

def admin_dashboard(request):
    return render(request,'barberwebapp/admin_dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)




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


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'barberwebapp/create_appointment.html', {'form': form})

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







    