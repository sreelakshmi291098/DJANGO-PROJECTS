from django.contrib import admin

# Register your models here.
from app13.models import Register
from app13.models import School

admin.site.register(Register)
admin.site.register(School)