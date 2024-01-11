from django.contrib import admin
from .models import Products, Category, Level, ReservedProduct

#from django.contrib import admin
#from .models import CustomUser

#admin.site.register(CustomUser)

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(ReservedProduct)