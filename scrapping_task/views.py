from django.shortcuts import render
from .models import User
from bs4 import * 
import requests as rq
import os


#view 1
def index(request):
    return render(request, 'index.html')
    

# view 1
def get_user(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        phone = request.POST.get('phone')
        user = User()
        user.name= name
        user.url = url
        user.phone_number = phone
        user.save()
        return render(request, 'home.html')
        
        
# view 2
def get_user_info(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        data = User.objects.filter(name__iexact=name)
        return render(request, 'home.html', {'datas': data})


# view 3
def get_images(request):
    images=[]
    if request.method == 'GET':
        return render(request, 'images.html')
    if request.method == 'POST':
        try:
            link = request.POST.get('link')
            r2=rq.get(link)
            soup2= BeautifulSoup(r2.text , "html.parser")
            x= soup2.select('img[src^="https://mir-s3-cdn-cf.behance.net/projects/404"]')

            for img in x:
                images.append(img['src'])

            
            return render(request, 'images.html', {'images' : images})
        except:
            error= "Invalid URL"
            return render(request, 'images.html', {'error' : error})

