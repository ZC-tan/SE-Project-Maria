from django.contrib import admin
from entity.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','password']

admin.site.register(User,UserAdmin)

class DocAdmin(admin.ModelAdmin):
    list_display = ['creator','body']
admin.site.register(Doc,DocAdmin)