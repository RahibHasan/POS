from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request,'index.html',{'title':'Dashboard','head_breadcumb':'Dashboard','href':'dashboard'})

def custom_login(request):
	if request.method == "POST":
		form = Custom_login_form(request.POST)
		# if form.is_valid():
		user_authneticate=authenticate(request,username=request.POST.get('username',None),password=request.POST.get('password',None))
		if user_authneticate is not None:
			login(request,user_authneticate)
			return HttpResponseRedirect(reverse('dashboard'))
		else:
			messages.error(request,'Your username & password is wrong try again ')
			return HttpResponseRedirect(reverse('custom_login'))
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('dashboard'))
		else:
			form = Custom_login_form()
			return render(request,'frontend/login.html',{'fields': form})
	return render(request,'frontend/login.html',{'fields': form})
