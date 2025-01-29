from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    Fobj = StudentForms() 
    Pobj = ProfileForm()
    d = {'Fobj':Fobj, 'Pobj':Pobj}
    
    # Here the user give its data in frontend and it store in the backend 
    if request.method == 'POST':
        obj1 = StudentForms(request.POST)
        obj2 = ProfileForm(request.POST, request.FILES)
        
        # Here we check the 2 obj is valid or not
        if obj1.is_valid() and obj2.is_valid():
            
            #* here the mutable of obj1 was started
            
            #! Here the pw was get from clean data after entering the password  by user
            pw = obj1.cleaned_data.get('password')
            
            #! Here the Commit = false----> (it is used to mutable an object data (it means we can change all the data in StudentForms(obj1)))
            Mobj1 = obj1.save(commit=False) 
            
            #! here the password again store into obj1 after mutable (in Mobj)
            Mobj1.set_password(pw)
            
            #! here we save this into database after mutable all the data in objects
            Mobj1.save()
            
            #* here the mutable of obj1 was end 
            
            #* here the mutable of obj2 start
            #! Here obj2 is getting mutable and we can update all the data inside the obj2 
            Mobj2 = obj2.save(commit=False)
            
            #! Here the username is in both the table so we have to match the table
            Mobj2.username = Mobj1
            
            #! Then we have to save this obj2 data in database (i.e profile form data)
            Mobj2.save()        
            #* Here the mutable object was end 
            return HttpResponse("<h1>Registration Done..........</h1>")
    return render(request,'register.html',d)
