from django.shortcuts import render
from .models import Car, Driver

from .forms import DriverForm, CarForm

def home(request):
    return render(request,"home.html", {})

def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)
    car_objs = Car.objects.filter(owner_id=owner_obj.id)
    context = {
        "vehicles": car_objs,
        "drivers": owner_obj,
    }
    return render(request, "car_detail.html", context)

def driver_detail(request):
    return render(request, 'driver_detail.html',{'drivers':Driver.objects.all()})

def driver_form(request):
    if request.method=="POST":
        form=DriverForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DriverForm()
    return render(request, 'driverform.html', {'form':form})

def car_form(request):
    if request.method=="POST":
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CarForm()
    return render(request, 'carform.html', {'form':form})

