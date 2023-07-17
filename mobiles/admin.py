from django.contrib import admin
from mobiles.models import *
# Register your models here.



class lap_admin(admin.ModelAdmin):
    list_display = ('name','brand','price','touch_screen')


admin.site.register(Laptop,lap_admin)