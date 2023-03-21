from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'city', 'state', "zipcode", "degree", 'school','graduation', "company", "position","start_date","end_date", "description"]
admin.site.register(Profile, ProfileAdmin)