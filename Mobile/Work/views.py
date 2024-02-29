from django.shortcuts import render,redirect
from django.views.generic import View
from Work.forms import MobileForm,Register,Signin
from Work.models import Mobile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator
#in our project (is a class based view)we use @decorator for a method inside the class

# Create your views here.

#create a decorator for usre authentication
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"You Should login first")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

# @method_decorator(signin_required,name='dispatch')





class MobileView(View):
    def get(self,request):
        form=MobileForm()
        return render(request,'mobile_add.html',{'form':form})

    def post(self,request):
        form=MobileForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Mobile added Successfully')

            form=MobileForm()
           
        else:
            messages.error(request,'Failed to added')
        return render(request,"mobile_add.html",{'form':form})

#Display all data in another page

@method_decorator(signin_required,name='dispatch')
class Mobilelist(View):
    def get(self,request):
        #if request.user.is_authenticated:
        #a way to tell if the user has been authenticated. 
        #user.is_authenticated: To check if a user has an active session on their device, use the request. user. is_authenticated variable—it will be True if a session is active 
        
        data=Mobile.objects.all()
        return render(request,'mobile_list.html',{'data':data})

#Search bar
    def post(self,request):
        brand=request.POST.get("brandname")
        data=Mobile.objects.filter(brand=brand)
        return render(request,'mobile_list.html',{'data':data})

#View Details 

@method_decorator(signin_required,name='dispatch')
class MobileDetail(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)

        id=kwargs.get("pk")
        qs=Mobile.objects.get(id=id)
        return render(request,"mobile_detail.html",{'data':qs})

#Delete a particular Mobile

class Mobile_delete(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Mobile.objects.get(id=id).delete()
        messages.success(request,'Deleted Successfully')
        return redirect('mobile-al')


#Update a record
@method_decorator(signin_required,name='dispatch')
class Mobile_update(View):
    def get(self,request,*args,**kwargs):
        data=kwargs.get('pk')
        obj=Mobile.objects.get(id=data)
        form=MobileForm(instance=obj) 
        return render(request,'mobile_update.html',{'form':form})

    def post(self,request,*args,**kwargs):
        data=kwargs.get("pk")
        obj=Mobile.objects.get(id=data)
        form = MobileForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Mobile Update Successfully')
        else:
            print("get out")
            messages.error(request,'Failed to Update')
        return redirect('mobile-al')


#Signup

class Signup(View):
    def get(self,request):
        form=Register()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            form=Register()
            messages.success(request,"Registration successfull")
        else:
            messages.error(request,'Registration Failed')
        return render(request,'register.html',{'form':form})

# Login or signin

class SigninView(View):
    def get(self,request):
        form=Signin()
        return render(request,'login.html',{"form":form})

    def post(self,request,*args,**kwargs):
        form=Signin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            form=Signin()

            print(u_name,pwd)

            user_obj=authenticate(request,username=u_name,password=pwd)
            #authenticate : only check if the username and pwd are present in the db

            if user_obj:
                print("Valid Credential")
                login(request,user_obj)

                print(request.user) #print the name user in terminal
                return redirect('mobile-al')
            else:
                print("Invalid Credential")
        else:
            print("get out")
        return render(request,'login.html',{"form":form})


#Logout or signout

class Signout(View):
    def get(self,request):
        logout(request)
        return redirect('login')