from .import views
from django.urls import  path
from .import  views
app_name='Car'

urlpatterns = [
    path('',views.index),
    path('parts_data',views.CarListView.as_view(),name='parts_data'),
]