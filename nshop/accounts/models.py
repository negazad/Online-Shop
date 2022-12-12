from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from .managers import UserManager
from flask_sqlalchemy import SQLAlchemy
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    user_name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    #* * * * *if i changed the usernamefield i must delete the fields from the required one*****
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'user_name', 'first_name', 'last_name', 'age']
    #**** in managers the order of argus for creatuser is based on userfield then requiredfield

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin

