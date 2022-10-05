
from django.urls import path
from .views import createProfile, deleteUser, hesap, profile, userLogin, userRegister,userLogout
urlpatterns = [
    path("register/",userRegister,name="register"),
    path("login/",userLogin,name="login"),
    path("logout/",userLogout,name="logout"),
    path("profile/",profile,name="profile"),
    path("create/",createProfile,name="create"),
    path("hesap/",hesap,name="hesap"),
    path("delete/",deleteUser,name="delete")
    
    ]