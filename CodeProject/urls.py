"""CodeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Common import views as cv
from . import settings
from django.conf.urls.static import static
from fileupload import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.Registration.as_view(),name='home'),
    path('registration/', cv.Registration.as_view(),name='registration'),
    path('userlogin/', cv.UserLogin.as_view(),name='userlogin'),
    path('logoutuser/', cv.LogoutView.as_view(),name='logoutuser'),
    path('dashboard/', fv.DashboardView.as_view(),name='dashboard'),
    path('addfile/', fv.UserFileView.as_view(),name='addfile'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
