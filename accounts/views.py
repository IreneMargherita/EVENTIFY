from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        address=request.POST['address']
        gender=request.POST['gender']
        #date_of_joining=request.POST['date_of_joining']
        #date_of_joining=date_of_joining1.replace("/","-")
        prior_experience=request.POST['prior_experience']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('USERNAME TAKEN')
                messages.info(request,"THE USERNAME IS TAKEN")
            elif User.objects.filter(email=email).exists(): 
                print('THIS ACCOUNT HAS ALREADY BEEN REGISTERED WITH THE EMAIL') 
                messages.info(request,"THIS ACCOUNT HAS ALREADY BEEN REGISTERED WITH THE EMAIL")
                #user=User.objects.create_user(username=username,password=password1,email=email,name=name,prior_experience=prior_experience,address=address,gender=gender,date_of_joining=date_of_joining)
                eciinfo=User(username=username,password=password1,email=email,name=name,prior_experience=prior_experience,address=address,gender=gender)#,date_of_joining=date_of_joining)  
                eciinfo.save()
                messages.info(request,"YOU NOW HAVE AN ECI ACCOUNT")
                print('USER CREATED')
        else:
            print('PASSWORD NOT MATCHING')
            messages.info(request,"THE PASSWORD DOES NOT MATCH")  
            return redirect('/')              
    return render(request,"register.html")
