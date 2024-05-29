from django.contrib import admin
from .models import Message, Room

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','sent_by','body','created_at','created_by']

admin.site.register(Room)