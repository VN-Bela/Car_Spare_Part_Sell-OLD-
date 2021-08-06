from .import  views
from django.urls import  path,include
from django.contrib.auth import views as auth_views


app_name='Car'

urlpatterns = [
    path('',views.CarListView.as_view(),name="Data"),
    # path('', views.index ,name="Data"),
    path('',include('django.contrib.auth.urls')),
    path('parts_data',views.CarCreateView.as_view(),name='parts_data'),
    path("car_detail/<str:pk>",views.CarDetailIndexView.as_view(),name="car_detail"),
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("signup/user",views.BuyerSignUpView.as_view(),name="user_signup"),
    path("signup/seller",views.SellerSignUpView.as_view(),name="seller_signup"),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    
    
   
   
]