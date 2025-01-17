from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from .models import User,Barber,Service, Appointment, WorkingHours, Reviews
from rest_framework import viewsets
from .serializers import BarberSerializer
from rest_framework.permissions import IsAuthenticated

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


class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]


    