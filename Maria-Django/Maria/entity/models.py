from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    password = models.CharField(max_length=15)

class Doc(models.Model):
    creator = models.CharField(max_length=100)
    title = models.CharField(max_length=50,default='New Document')
    content = RichTextField(blank=True,null=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_recycled = models.BooleanField(default=False)
    is_group_doc = models.BooleanField(default=False)
    doc_group_id = models.IntegerField(null=True,blank=True)
    modify_right = models.BooleanField(default=True)
    others_modify_right = models.BooleanField(default=True)


class DocUser(models.Model):
    document_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100)
    is_favourited = models.BooleanField(default=False)
    modified_time = models.DateTimeField(auto_now=True)

class Group(models.Model):
    groupname = models.CharField(max_length=100)
    leader_name = models.CharField(max_length=100,null=True)

class GroupMember(models.Model):
    group_id = models.IntegerField(null=True)
    user_name = models.CharField(max_length=100)
    others_create_right = models.BooleanField(default=True)
    others_recycle_right = models.BooleanField(default=False)

class InviteMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    group_id = models.IntegerField(null=True)
    is_accept = models.BooleanField(null=True,blank=True)
    content = models.CharField(max_length=400,null=True,blank=True)
    # document_id = models.IntegerField
