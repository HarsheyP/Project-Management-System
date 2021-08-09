from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib import messages


from rest_framework.decorators import api_view

from rest_framework.response import Response

# Create your views here.
from .models import *
from board.models import *
from .forms import CreateUserForm
from .forms import LoginForm

##############baseindexpage######################################
def home(request):
    return render(request,"base.html", {'title':'index'})

######################register here###############################


def signupview(request):
    #if request.user.is_authenticated:
     #   return redirect('board:dashboard')
    #else:
        #form=CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                email=form.cleaned_data.get('email')
                messages.success(request, 'Account created successfully')
                return redirect('accounts:home')
                #return HttpResponse("User created successfully")
        else:
            form = CreateUserForm()
        return render(request,'register/signup.html',{'form':form , 'title':'register here'})
        


def loginpage(request):
    #if request.user.is_authenticated:
     #   return render(request, 'base.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('board:dashboard')
        else:
            form = LoginForm(request.POST)
            return render(request,'register/login.html',context={"login_form":form})
    else:
        form = LoginForm()
        return render(request,'register/login.html',context={"login_form":form})
   # return render(request,'register/login.html',context={"login_form":form})
 

#@login_required(login_url="login/")

def logoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('accounts:home')
# when entered to admin shows messages, 
# unable to redirect to dashboard

@api_view(['GET'])
def category_collection(request):
    if request.method == 'GET':
        posts = Board.objects.all().filter(user__username=request.user)
        serializer = BoardSerializer(posts, many=True)
        return Response(serializer.data)
