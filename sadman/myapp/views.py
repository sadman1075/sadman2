from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from myapp.models import sadman

# Create your views here.
def userwork(request):
  if request.method=="POST":
    user=sadman()
    user.username=request.POST.get('username')
    user.city=request.POST.get('city')
    user.thana=request.POST.get('thana')
    user.area=request.POST.get('area')
    user.images=request.FILES.get('images')
    user.save()
    return HttpResponse("submitted")

    



  return render(request,'userwork.html')

def home(request):

  return render(request,'home.html')

def glasswaste1(request):
    return render(request,'glasswaste.html')


def plasticswaste1(request):
    return render(request,'plasticswaste.html')
def medicalwaste2(request):
    return render(request,'medicalwaste.html')
def constructionwaste1(request):
    return render(request,'constructionwaste.html')

def aboutus(request):
    return render(request,'aboutus.html')


def contract(request):
    return render(request,'contract.html')




def loginpage(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(request,username=username,password=password)
       
             
         if user is not None:
              login(request,user)
              return redirect("userwork")
         else:
              messages.error(request,'please enter your valied user name and password')

    return render (request,'sadman.html')

def singuppage(request):   
    
        if request.method=="POST":
         uname=request.POST.get('name')
         email=request.POST.get('email')
         pass1=request.POST.get('pass1')
         pass2=request.POST.get('pass2')
      


         if User.objects.filter(email=email).exists():
              messages.error(request,'This email is already use')
              return redirect('singup')
         if pass1 and pass2 is not None:
       
              if pass1==pass2:
             
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save() 
    
                return redirect("login")
              else:
          
               messages.error(request,'Password and confirm password is not same')
               return redirect('singup')
         else:
             messages.error(request,'please enter your password')
 
       
    
        return render(request,'sadman1.html')



