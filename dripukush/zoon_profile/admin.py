from django.contrib import admin
from .models import Zoon_Profile
# Register your models here.
@admin.register(Zoon_Profile)
class Zoon_ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'zoon_name']
 