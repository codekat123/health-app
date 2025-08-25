from django.db import models
from  django.contrib.auth.models import BaseUserManager , AbstractBaseUser , PermissionsMixin
import pycountry


class MyaccountManager(BaseUserManager):
     def create_user(self,email,first_name,last_name,user_name,country,phone_number,password=None,**extra):
          if not email:
               raise ValueError("user must have email address")
          if not user_name:
               raise ValueError("use must create username ")
          email = self.normalize_email(email)
          user = self.model(
               email = email,
               first_name = first_name,
               last_name = last_name,
               user_name = user_name,
               country = country,
               phone_number = phone_number
          )                 
          if not password:
               raise ValueError('users must enter their password')
          user.set_password(password)
          user.save(using=self._db)
          return user
     def create_superuser(self,email,first_name,last_name,user_name,country,phone_number,password=None,**extra):
          user = self.create_user(
               email = email,
               first_name = first_name,
               last_name = last_name,
               user_name = user_name,
               country = country,
               phone_number = phone_number,
               password = password
          )
          user.is_superuser = True
          user.is_staff = True
          user.is_active = True
          user.save(using=self._db)
          return user
     

class Account(AbstractBaseUser,PermissionsMixin):
     @staticmethod
     def get_country():
          countries = [(c.alpha_2,c.name) for c in pycountry.countries]
          return countries

     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     email = models.EmailField(max_length = 60,unique=True)
     user_name = models.CharField(max_length=50,unique=True)
     country = models.CharField(max_length=50,choices=get_country())
     is_staff = models.BooleanField(default=False)
     is_active =  models.BooleanField(default=False)
     phone_number = models.CharField(max_length=50)
     create_at = models.DateTimeField(auto_now_add=True)
     datajoined =models.DateTimeField(auto_now_add=True)

     objects = MyaccountManager()
     
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['first_name','last_name','country','user_name']
     
     def __str__(self):
          return self.first_name
          
