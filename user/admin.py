from django.contrib import admin
from .models import Account, Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Account)