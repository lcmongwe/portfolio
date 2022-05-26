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

def search_category(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        name=Image.objects.filter(name__contains=searched)
        return render(request, 'searched_images.html',{'searched':searched,'name':name,})
       

    else:
        return render(request, 'searched_images.html',{})
