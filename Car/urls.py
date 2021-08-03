from .import views
from django.urls import  path
from .import  views
app_name='Car'

urlpatterns = [
    path('',views.CarListView.as_view(),name="Data"),
    # path('', views.index ,name="Data"),
    path('parts_data',views.CarCreateView.as_view(),name='parts_data'),
    path("car_detail/<str:pk>",views.CarDetailIndexView,name="car_detail"),
   
]