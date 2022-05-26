from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Image,Location,Category


# Create your views here.

def home(request):
    # event_list=Event.objects.all().order_by('-name')
    return render(request, 'home.html',{})
