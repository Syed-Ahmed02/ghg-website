from ast import Or
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank = True)
    category = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Execs(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank = True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name    

