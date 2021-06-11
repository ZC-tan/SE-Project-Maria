from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=15)

class Doc(models.Model):
    creator = models.CharField(max_length=100)
    body = RichTextField(blank=True,null=True)
