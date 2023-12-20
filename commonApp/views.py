from django.shortcuts import render, redirect 
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.db.models import Max
from django.db import transaction

from commonApp.models import *
from accounting.models import *
from login.models import *
# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Notification

def get_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user, read=False)
    notifications_data = [{'message': notification.message, 'timestamp': notification.timestamp} for notification in notifications]
    return JsonResponse({'notifications': notifications_data})

def mark_notifications_as_read(request):
    user = request.user
    Notification.objects.filter(user=user, read=False).update(read=True)
    return JsonResponse({'success': True})


@login_required(login_url='login')
# def voucher(request):
 
#     return render(request,'voucher.html')

@login_required(login_url='login')
def profile(request):
    profilePic='http://127.0.0.1:8000'+request.user.profilePic.url
 
    return render(request,'profile.html',{'user':request.user,'profilePic':profilePic})


@login_required(login_url='login')
def profile(request):
    profilePic='http://127.0.0.1:8000'+request.user.profilePic.url
 
    return render(request,'home.html',{'user':request.user,'profilePic':profilePic})