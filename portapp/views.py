from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Image,Location,Category


# Create your views here.

def home(request):
    image_list=Image.objects.all().order_by('name')
    return render(request, 'home.html',{'image_list':image_list})

def big_image(request,image_id):
    image=Image.objects.get(pk=image_id)
    return render(request, 'big_image.html',{'image':image,})