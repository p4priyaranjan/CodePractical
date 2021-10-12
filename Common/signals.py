from django.contrib.auth.signals import user_logged_in,user_login_failed
from .models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
# from django.contrib.gis.utils import GeoIP

@receiver(user_login_failed,)
def login_failed(sender, credentials, **kwargs):
    print(credentials)
    user=get_object_or_404(CustomUser,phone_number=credentials['phone_number'])
    if user is not None:
        lal=int(user.login_attempts_left)
        if lal>0:
            user.login_attempts_left=lal-1
        else:
            user.is_active=False


@receiver(post_save, sender=CustomUser)
def registration_success(sender, request, instance,created, **kwargs):
    if created:
        ip = request.META.get('REMOTE_ADDR', None)
        # gip=GeoIP()
        if ip:
            request.session['ip'] = ip
            # request.session['city'] = gip.city(ip)['city']
            # request.session['country']=gip.country(ip)['country']
            request.session['city'] = 'NA' 
            request.session['country']='NA'
        else:
            request.session['city'] = 'NA' 
            request.session['country']='NA'
    
