
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import *


from .forms import *
from .models import *
# Create your views here.
def userRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        resim = request.FILES['resim']
        tel = request.POST['tel']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Bu kullanıcı adı zaten kullanılmış")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Bu Email  zaten kullanılmış")
                return redirect("register")
            elif username in password1:
                messages.error(request,"kullanıcı adı şifreye benzeyemez")
                return redirect("register")
            elif len(password1) < 6:
                messages.error(request,"şifre en az 6 karakter olmalı")
                return redirect("register")
            else:
                user = User.objects.create_user(username = username,password = password1,email=email) 
                Account.objects.create(
                    user = user,
                    resim = resim,
                    tel = tel
                )
                user.save()
                messages.success(request,"Başarıyla kaydoldunuz.")
                return redirect("index")
    return render(request,"user/register.html")
def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"Giriş Başarılı")
            return redirect("profile")  
        else:
            messages.error(request,"Yanlış kullanıcı adı veya şifre")
            return redirect("login")
    return render(request,"user/login.html")  
def userLogout(request):
    logout(request)
    messages.success(request,"Çıkış Yaptınız")
    return redirect("index")

def profile(request):
    profile = Profile.objects.all()
    context = {
        "profile":profile
    }
    return render(request,"browse.html",context) 
def createProfile(request):  
    form = ProfileForm()
    profile = Profile.objects.filter(user = request.user)
    if(len(profile) < 4): 
       if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
           profil = form.save(commit=False)
           profil.user = request.user
           profil.save()
           messages.success(request,"Profil Oluşturuldu")
           return redirect("profile")
    else:
        messages.error(request,"Profil sayısı 4'ü geçemez")
        return redirect("profile")       
    context = {
        'form':form
    }
    return render(request,"createProfile.html",context)       

def hesap(request):
    user = request.user.account
    context = {
       "user":user
    }   
    return render(request,"user/hesap.html",context)

def deleteUser(request):
    user = request.user
    user.delete()
    messages.success(request,"Kullanıcı silindi")
    return redirect("index.html")