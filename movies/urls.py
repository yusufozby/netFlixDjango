
from django.urls import path
from .views import index, movies, videolar
urlpatterns = [
    path('',index,name="index"),
    path('movies/<int:profileId>',movies,name="movies"),
    path("video/<int:id>",videolar,name="video")
    
]