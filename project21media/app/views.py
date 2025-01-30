from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    Robj = RegisterForm()
    Pobj = ProfileForm()
    d = {'Robj':Robj,'Pobj':Pobj}
    
    if request.method == 'POST':
        obj1 = RegisterForm(request.POST)
        obj2 = ProfileForm(request.POST, request.FILES)
        if obj1.is_valid() and obj2.is_valid():
            pw = obj1.cleaned_data.get('password')
            
            Mobj1 = obj1.save(commit=False)
            Mobj1.set_password(pw)
            Mobj1.save()
            
            Mobj2 = obj2.save(commit=False)
            Mobj2.username = Mobj1
            Mobj2.save()
            return HttpResponse("<h1>Register Done.......</h1>")
    return render(request,'register.html',d)
