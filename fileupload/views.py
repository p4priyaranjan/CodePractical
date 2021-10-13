from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate, forms,login,logout
from django.views.generic import View
from .forms import UserFileForm
from .models import UserFile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserFileView(View):
    def get(self,request,*args, **kwargs):
        fm=UserFileForm()
        # print(fm)
        return render(request,'fileupload/addfile.html',{'form':fm})

    def post(self,request,*args, **kwargs):
        form=UserFileForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            file=form.cleaned_data['my_file']
            user=request.user
            fi=UserFile(file,user)
            fi.save()
            return HttpResponseRedirect('/dashboard/')
        fm=UserFileForm(request.POST)
        return render(request,'Common/addfile.html',{'form':fm})

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self,request,*args, **kwargs):
        file=UserFile.objects.filter(user=request.user)
        return render(request,'fileupload/dashboard.html',{'fs':file})
