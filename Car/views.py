from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based View
def index(request):
    #return HttpResponse("Welcome to Car Part Selling ")
    return render(request,'Car/index.html')

# class based View
