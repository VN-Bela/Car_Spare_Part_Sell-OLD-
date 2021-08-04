from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login
# Create your views here.
from .forms import LoginForm
from django.views import View

class LoginView(View):
  
    template_name="login_reg/login.html"
    def post(self,request):
        form=LoginForm(request.post or None)
        if form.is_valid():
            user=authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user==None:
                #attempt=request.session.get('attempt') or 0 
                #request.session['attempt']=attempt+1
                #return redirect("/invalid-password")
                request.session['invalid_user']=1 # 1= True 
                return render(request,'login_reg/login.html',{'form':form,'invalid_user':True})

