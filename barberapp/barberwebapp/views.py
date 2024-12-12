from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'barberwebapp/index.html')


def home(request):
    return render(request,'barberwebapp/home.html')


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
    