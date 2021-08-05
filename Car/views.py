from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import Car,User,Seller
from django.contrib.auth import login
from .forms import Car_Part_Form,SellerSignUpFrom,UserSignupForm

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
    form_class=Car_Part_Form
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

# Userview
class UserSignUpView(CreateView):
    model=User
    form_class=UserSignupForm
    template_name='Car/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type']='user'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('Car:parts_data')

#seller Signup
class SellerSignUpView(CreateView):
    model=User
    form_class=SellerSignUpFrom
    template_name="Car/signup_form.html"
    def get_context_data(self, **kwargs):
        kwargs['user_type']='seller'
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('Car:parts_data')


    


