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



@login_required(login_url='login')
def profile(request):
    profilePic='http://127.0.0.1:8000'+request.user.profilePic.url
 
    return render(request,'profile.html',{'user':request.user,'profilePic':profilePic})