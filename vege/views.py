from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Note : CREATE operation in CRUD
# in these business logic we can get data fron front end side ( from receies.html : from form) 

@login_required(login_url="/login/")   # we applied decorator to receipes page mens user cant go directly to 
                                       # receipes pages insted of it first go to login page.
                                       # we can apply this decoroator obefore any page


def receipes(request):
    if request.method == "POST":
        
        
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,

    )
        return redirect('/receipes/')


    # Note : READ operaton in CRUD
    # here we can read data from model (database) and render into front end (receipes.html)
        
    queryset = Receipe.objects.all()

    # Note : READ operaton with search option in CRUD
    # if you search with name then according search record will show

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    # if you not search with name then then all record will show
    context = {'receipes':queryset}
    return render(request,'receipes.html',context)


# Note : UPDATE operaton in CRUD
# here we can GET data from model (database) and update it render into front end (receipes.html)

def update_receipe(request,id):
     queryset = Receipe.objects.get(id=id)

     if request.method =="POST":
         data = request.POST
         receipe_image = request.FILES.get('receipe_image')
         receipe_name = data.get('receipe_name')
         receipe_description = data.get('receipe_description')

         queryset.receipe_name = receipe_name
         queryset.receipe_description = receipe_description
         if receipe_image:
             queryset.receipe_image = receipe_image
             
         queryset.save()
         return redirect('/receipes/')


    
     context = {'receipe':queryset}
     return render(request,'update_receipes.html',context)




# Note : DELETE operaton in CRUD
# from here we can get dynamic id and delete record of that id

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


# login code : we get data from login.html page
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if username is not matched then show error message
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid user name")
            return redirect('/login/')
        
        # if password is not matched then show error message
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        
        # if user name and password is matched then accept and goto receies page
        else:
            login(request , user)
            return redirect('/receipes/')


    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')






# Note : Regiseter page logic here for that we import : from django.contrib.auth.models import User
# here we get data from register.html page and insert into predefined User model 
def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        # if username is already exists then not register with that name and give error msg
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')

         # if username is unique then insert data into predifined User model
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
                )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfuly")

        return redirect('/register/')

    return render(request,'register.html')


def get_students(request):
    queryset = Student.objects.all()

    

    paginator = Paginator(queryset, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request,'report/students.html',{'queryset':page_obj})