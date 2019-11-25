from django.db import models
import os
import random
import requests
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.core.validators import RegexValidator
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserManager(BaseUserManager):
    def Create_user(self,phone,password=None):
        if not phone:
            raise ValueError('user must have phone number')
        if not password:
            raise ValueError('user must have  password')
        
        user_obj=self.model(
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.save(using=self.db)
    def create_superuser(self,phone,password=None):
        if not phone:
            raise ValueError('user must have phone number')
        if not password:
            raise ValueError('user must have  password')
        
        user_obj=self.model(
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.save(using=self.db)
    

class User(AbstractBaseUser):
   # phone_regex=RegexValidator(regex=r'^\+?1?\d{9,10}$',messeg="phone Number must be entered in the format: '999999999'. Only 10 digits")
    phone =models.CharField(max_length=10,unique=True)
    is_active = models.BooleanField(default=True)
    # this field is required to login super user from admin panel
    is_staff = models.BooleanField(default=True)
    # this field is required to login super user from admin panel
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    object = UserManager()

    def __str__(self):
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_superuser

class PhoneoTP(models.Model):
    phone=models.CharField(max_length=10,unique=True)
    otp=models.CharField(max_length=9,blank=True,null=True)
    count=models.IntegerField(default=0,help_text="Number of otp send")


    def __str__(self):
        return str(self.phone)+'is sent'+str(self.otp)
