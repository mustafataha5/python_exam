from django.shortcuts import render,redirect,HttpResponse
from .models import User,Trip
import bcrypt
from django.contrib import messages
import datetime

# Create your views here.
def index(request):
    if 'userID' in request.session:
        #messages.success(request,"Welcome back from last session")
        return redirect('exam:main_page')
    
    return redirect('exam:reg&login')

def registeration_and_login(request):
    return render(request,'index.html')       


def create_user(request):
    if request.method == "POST": 
        errors = User.objects.basic_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        
        user_fname = request.POST['first_name'].capitalize() 
        user_lname = request.POST['last_name'].capitalize()
        email =  request.POST['email'] 
        hash_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
        user = User.objects.create(first_name=user_fname,last_name=user_lname,email=email,password=hash_password)    
      
        
        request.session['userID'] =user.id 
        #messages.success(request,"Successful registeration ")
        
        return redirect('exam:main_page')    

def main_page(request):
    if not 'userID' in request.session:
        messages.warning(request,'You need to regiester or login',extra_tags='invalid_accuess')
        return redirect('/')
    data={
        "user":User.objects.get(id=request.session['userID']),
        'trips': Trip.objects.all(),
    }
    
    return render(request,'main_page.html',data)

def login_user(request):
    if request.method == "POST": 
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        user = User.objects.get(email=request.POST['email'])    
        request.session['userID'] = user.id
        #messages.success(request,"Successful login ")
        return redirect('exam:main_page')  

def logout(request):
    request.session.clear()
    return redirect("/")



def new_trip(request):
    if not 'userID' in request.session:
        messages.warning(request,'You need to regiester or login',extra_tags='invalid_accuess')
        return redirect('/')
    userID = int(request.session['userID'])
    data={
        'user': User.objects.get(id=userID),
        'current_date':datetime.datetime.today()
    }
    return render(request,"new_trip.html",data)



def create_trip(request):
    if request.method == 'POST': 
        errors = Trip.objects.trip_vaildation(request.POST)
        
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/trips/new')   
        trip_destination = request.POST['destination'].capitalize()
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        iter=request.POST['itinerary']
        userID = request.session['userID']
        user = User.objects.get(id=userID)
        trip = Trip.objects.create(destination=trip_destination,start_date=start_date,end_date=end_date,desc=iter,created_by=user)
        #trip.travelers.add(user)## for testing 
        ## set the creater user in the travel he made 
        messages.success(request,"Successful created trip.")
    return redirect('exam:main_page')

def show_trip(request,tripID):
    trip = Trip.objects.get(id=tripID)
    if not 'userID' in request.session :
        return redirect('exam:main_page')
    userID = int(request.session['userID'])
    data = {
        'user' : User.objects.get(id=userID),
        'trip' : trip,
    }
    return render(request,'show_trip.html',data)

def edit_trip(request,tripID):
    trip = Trip.objects.get(id=tripID)
    
    if  not 'userID' in request.session and  trip.created_by.id != int(request.session['userID']):
        return redirect('exam:main_page')
    userID = int(request.session['userID'])
    data = {
        'user' : User.objects.get(id=userID),
        'trip' : trip,
    }
    return render(request,'edit_trip.html',data) 

def update_trip(request,tripID):
    
    if request.method == 'POST' : 
        errors = Trip.objects.trip_vaildation(request.POST)
        
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect(f'/trips/edit/{tripID}')   
        
        trip = Trip.objects.get(id=tripID)
        trip.destination = request.POST['destination'].capitalize()
        trip.start_date = request.POST['start_date']
        trip.end_date = request.POST['end_date']
        trip.desc=request.POST['itinerary']
        trip.save()
        messages.success(request,"Successful update trip.")
    return redirect('exam:main_page')

def delete_trip (request,tripID):
    trip = Trip.objects.get(id=tripID)
    trip.delete()
    return redirect('exam:main_page')


def show_mytrip(request):
    
    if  not 'userID' in request.session :
        return redirect('exam:main_page')
    userID = int(request.session['userID'])
    user = User.objects.get(id=userID)
    user_trips = user.trips.all().values('id')
    ex_trips = Trip.objects.exclude( id__in=user_trips)
    data = {
        'user': User.objects.get(id=userID),
        'ex_trips': ex_trips,
    }
    
    return render(request,'show_mytrip.html',data)



def join_trip(request,tripID):
    
    if  not 'userID' in request.session :
        return redirect('exam:main_page') 
    
    userID = int(request.session['userID'])
    user = User.objects.get(id=userID)
    trip = Trip.objects.get(id=tripID)
    trip.travelers.add(user)
    
    return redirect('/trips/mytrip')


def cancel_trip(request,tripID):
    
    if  not 'userID' in request.session :
        return redirect('exam:main_page') 
    
    userID = int(request.session['userID'])
    user = User.objects.get(id=userID)
    trip = Trip.objects.get(id=tripID)
    trip.travelers.remove(user)
    
    return redirect('/trips/mytrip')



