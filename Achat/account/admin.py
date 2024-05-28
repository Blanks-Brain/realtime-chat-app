from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','role','email','date_joined','last_login','is_active','is_staff']