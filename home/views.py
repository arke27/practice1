from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Note : when you simply show static data on html page
    # return HttpResponse("Hey am a django server")
    # return render(request,"home/index.html")


    # Note : when you show data from backend to html page (template)
    peoples = [
        {"name":"shiva",'age':22},
        {"name":"rama",'age':23},
        {"name":"gita",'age':24},
        {"name":"ravan",'age':25},

    ]
    vegetables = ['Pumpkin','Tomato','Potato']
    return render(request,"home/index.html",context={'page':'Home','peoples':peoples,'vegetables':vegetables})

def about(request):
    context = {'page':'About'}
    return render(request,"home/about.html",context) 

def contact(request):
    context = {'page':'Contact'}
    return render(request,"home/contact.html",context) 