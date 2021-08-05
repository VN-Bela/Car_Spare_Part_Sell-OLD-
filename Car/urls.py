from .import  views
from django.urls import  path


app_name='Car'

urlpatterns = [
    path('',views.CarListView.as_view(),name="Data"),
    # path('', views.index ,name="Data"),
    path('parts_data',views.CarCreateView.as_view(),name='parts_data'),
    path("car_detail/<str:pk>",views.CarDetailIndexView.as_view(),name="car_detail"),
    #path("Car/signup",views.SignupView.as_view(),name="signup"),
    path("signup/user",views.UserSignUpView.as_view(),name="user_signup"),
    path("signup/seller",views.SellerSignUpView.as_view(),name="seller_signup"),
    
   
   
]