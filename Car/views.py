from django.shortcuts import render
from django.http import HttpResponse
from django.views import  generic
from django.views.generic import ListView,CreateView
from .models import Car
from .forms import Car_Part_Form

# Create your views here.
# function based View
def index(request):
    # return HttpResponse("Welcome to Car Part Selling ")
   return render(request,'Car/index.html')

# class based View
class CarListView(ListView):
    # model=Car
    queryset = Car.objects.all()
    template_name='Car/index.html'
    # def get_queryset(self, request):
    #     context = Car.objects.all()
    #     return context

class CarCreateView(CreateView):
    model=Car
    template_name='Car/CarHome.html'
    fields=[
            'Car_name',
            'Car_model',
            'Car_Part_Name',
            'Car_Part_Info',
            'Car_Part_Cat',
            'Car_Part_Discription',
            'Owner_info',
        ]
    def form_valid(self,form):
        form.save()
    
class CarDetailIndexView(ListView):
    model=Car
    template_name="Car/Car_detail.html"

    


