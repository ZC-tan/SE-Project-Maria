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

class DocUser(models.Model):
    document_id = models.IntegerField
    user_id = models.IntegerField
    is_favourited = models.BooleanField(default=False)
    modified_time = models.DateTimeField(auto_now=True)

class Group(models.Model):
    groupname = models.CharField(max_length=100)
    leader_id = models.IntegerField

class GroupMember(models.Model):
    group_id = models.IntegerField
    user_id = models.IntegerField
    
