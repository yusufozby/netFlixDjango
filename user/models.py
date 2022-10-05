
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    resim = models.FileField(upload_to="profiles/")

    isim = models.CharField(max_length=250)
    

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)   
    resim = models.FileField(upload_to="profilresimleri/",null=True) 
    tel = models.IntegerField()

   
            

