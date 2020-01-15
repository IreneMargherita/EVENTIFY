from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Details,Progress,Images,Gallery
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'coverpage.html')

def team(request):
    gallery=Gallery.objects.all()
    return render(request,'team.html',{'gallery':gallery})   
     
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')

def quiz(request):
    return render(request,'quiz.html')

def login(request):
    if request.method == "POST":
        try:
            if Details.objects.filter(email=request.POST['email']).filter(password=request.POST['password']).exists():
                details=Details.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])
                progress = details.progress_set.all()
                images=details.images_set.all()
                your_page=[details,progress,images]
            else:
                return render(request, 'login.html', {'error': 'Email or password is incorrect.'})
        except Details.DoesNotExist:
           details = None
           return render(request, 'login.html', {'error': 'Email or password is incorrect.'})
        return render(request,"index.html",{'your_page':your_page})    
    else:
        return render(request, 'login.html')

    

def forgotpassword(request):
    return render(request,'forgotpassword.html')  

def clientregister(request):
    return render(request,'clientregister.html')      



def eciuser(request):
    images=Images.objects.all()
    
    
    
    return render(request,'index.html',{'images':images})


def register(request):
     return render(request,"register.html")

def validate_credentials(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        address=request.POST['address']
        gender=request.POST['gender']
        prior_experience=request.POST['prior_experience']
        if password1==password2:
            if Details.objects.filter(username=username).exists():
                print('USERNAME TAKEN')
                messages.info(request,"THE USERNAME IS TAKEN")
            elif Details.objects.filter(email=email).exists(): 
                print('THIS ACCOUNT HAS ALREADY BEEN REGISTERED WITH THE EMAIL') 
                messages.info(request,"THIS ACCOUNT HAS ALREADY BEEN REGISTERED WITH THE EMAIL")
                
            else:
                eciinfo = Details()
                eciinfo.name = name
                eciinfo.email = email
                eciinfo.username = username
                eciinfo.password = password1
                eciinfo.prior_experience = prior_experience
                eciinfo.address = address
                eciinfo.gender=gender
                eciinfo.save()
                progress=Progress(email=email,level=0,no_of_events_conducted=0,rating=0,digital_badge=0,score=0)
                progress.save()
                return render(request,'login.html')

        else:
            print('PASSWORD NOT MATCHING')
            messages.info(request,"THE PASSWORD DOES NOT MATCH. PLEASE TRY AGAIN")  
            return render(request,'register.html')           

    return render(request,'register.html')
def log_cred(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if Details.objects.filter(email=email).filter(password=password).exists():
            details=Details.objects.filter(email=email).filter(password=password).values()
            reg=Progress.objects.filter(email=email).values()
            #print(reg[0]['score'])
            #print('this the forign key')
            rd=[]
            rd.append(details[0]['name'])
            rd.append(reg[0]['score'])
            #rg=reg[0]['score']
            print(rd)

    else:
        print('invalid user')
        return render(request,"login.html")
    
    images=Images.objects.all()
    
    
    
    #return render(request,'index.html',{'images':images})    
    return render(request,'index.html',{'rd':rd,'images':images})   