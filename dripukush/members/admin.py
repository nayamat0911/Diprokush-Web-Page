from django.contrib import admin
from .models import Office, ZoonList, Members
# Register your models here.
admin.site.register(ZoonList)
admin.site.register(Members)
admin.site.register(Office)