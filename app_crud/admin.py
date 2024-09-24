from django.contrib import admin
from app_crud.models import User
# Register your models here.

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id",'name','email','pwd']