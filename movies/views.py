from django.shortcuts import render
from .models import *
from  user.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def movies(request,profileId):
    profile = Profile.objects.get(id = profileId)
    profiles = Profile.objects.filter(user = request.user)
    filmler = Movies.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        filmler = Movies.objects.filter(isim__icontains = search)
    context = {
        "filmler":filmler,
        "profile":profile,
        "profiles":profiles,
        'search':search
    }
    return render(request,"browse-index.html",context)    
def videolar(request,id):
    video = Movies.objects.filter(id = id)
    context = {
        "video":video
    }
    return render(request,"video.html",context)    
 