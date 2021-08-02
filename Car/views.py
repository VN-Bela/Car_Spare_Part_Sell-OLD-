from django.shortcuts import render
from django.http import HttpResponse
from django.views import  generic
from django.views.generic import ListView,CreateView
from .models import Car
from .forms import Car_Part_Form

# Create your views here.
# function based View
def index(request):
    #return HttpResponse("Welcome to Car Part Selling ")
    return render(request,'Car/index.html')

# class based View
class CarListView(ListView):
    model=Car
    template_name='Car/CarHome.html'
    def get_queryset(self):
        context = Car.objects.all()
        return context

class CarCreateView(CreateView):
    model=Car
    fields=['Car_name']

    


