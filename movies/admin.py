from django.contrib import admin

from movies.models import Kategori, Movies

# Register your models here.
admin.site.register(Movies)
admin.site.register(Kategori)