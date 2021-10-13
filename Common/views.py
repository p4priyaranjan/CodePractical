from django.contrib.auth import authenticate, forms,login,logout
from django.core.checks import messages
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from .models import CustomUser
import datetime 

from .forms import SignUpForm,LoginForm

class UserLogin(View):
    def get(self,request):
        fm=LoginForm()
        return render(request,'Common/login.html',{'form':fm})
    
    def post(self,request):
        fm=LoginForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=get_object_or_404(CustomUser,phone_number=uname)
#             print(user)
            if user is not None:
                locked = cache.get('Is_User_Locked', False, version=user.pk)
#                 print(locked)
                if not locked:
#                     user.is_active=True
                    user.login_attempts_left=3
                    user.save()
                    user=authenticate(username=uname,password=upass)
                    print(user)
                    if user is not None:
                        login(request,user)
                        messages.success(request,'User Logged In Successfully')
                        return HttpResponseRedirect('/dashboard/')
                    else:
                        return HttpResponseRedirect('/userlogin/')
                else:
                    return HttpResponseRedirect('/userlogin/') 
            else:
                return HttpResponseRedirect('/userlogin/')
        fm=LoginForm(request.POST)
        return render(request,'Common/login.html',{'form':fm})

class LogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/userlogin/')

class Registration(View):
    def get(self,request,*args, **kwargs):
        fm=SignUpForm()
        print(fm)
        return render(request,'Common/signup.html',{'form':fm})

    def post(self,request,*args, **kwargs):
        form=SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            phone_number=form.cleaned_data['phone_number']
            user_name=form.cleaned_data['user_name']
            email=form.cleaned_data['email']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password1']
            user=CustomUser.objects.create_user(phone_number=phone_number,first_name=first_name,last_name=last_name,user_name=user_name,email=email,password=password)
            print(user)
            messages.success(request,'Congratulations!! Please Login to continue ')
            return HttpResponseRedirect('/userlogin/')
        fm=CustomUser(request.POST)
        return render(request,'Common/signup.html',{'form':fm})


