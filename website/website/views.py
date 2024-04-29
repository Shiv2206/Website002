from django.http import HttpResponse
from django.shortcuts import render
from product.models import product
from signup.models import signup



# Create your views here.



def Home(request):
        prod=product.objects.all().order_by("product_Name")
        print(prod)
        context={
                'prod':prod
        }
        
        return render(request,"Home.html",context)

def about(request):
       
         try:
                 
               n1 = int(request.GET.get('n1'))
               n2 = int(request.GET.get('n2'))
         except (ValueError, TypeError):
    # Handle the error by returning an error message or a default value
              n1 = 0
              n2 = 0

         print(n1 + n2)
     
         return render(request,'about.html')


def contact(request):
        return render(request,'Contact.html')

def Log(request):
        return render(request,"log.html")


def register(request):
         if request.method == "POST":
                 Fname=request.POST["name"]
                 lname=request.POST["lastname"]
                 uname=request.POST["username"]
                 email=request.POST["email"]
                 password=request.POST["password"]
                 cpass=request.POST["confirmpassword"]
                 reg=signup( First_name=Fname,  Last_name=lname,  User_name=uname,  Email=email,Password=password,C_Pass=cpass)
                 reg.save()      
         return render (request,"register.html")
    
          
        