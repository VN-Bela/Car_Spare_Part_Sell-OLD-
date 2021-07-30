from .import views
from django.urls import  path

app_name='Car'

urlpatterns = [
    path('',views.index),
]