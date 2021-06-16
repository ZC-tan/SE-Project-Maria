from django.contrib import admin
from entity.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','password']

admin.site.register(User,UserAdmin)

class DocAdmin(admin.ModelAdmin):
    list_display = ['id','title','content']
admin.site.register(Doc,DocAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','groupname','leader_name']
admin.site.register(Group,GroupAdmin)

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ['id','group_id','user_name']
admin.site.register(GroupMember,GroupMemberAdmin)

class InvitationAdmin(admin.ModelAdmin):
    list_display = ['id','sender_name','receiver_name','group_id','is_accept','content']
admin.site.register(InviteMessage,InvitationAdmin)