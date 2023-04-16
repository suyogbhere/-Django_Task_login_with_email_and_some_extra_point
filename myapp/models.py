from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from. managers import CustomUserManager
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    first_name= models.CharField(max_length=250)
    email= models.EmailField(_('Email Address'),unique=True)
    mobile= models.CharField(max_length=10)
    status= models.BooleanField(default=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['mobile']
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin = models.BooleanField('Is admin',default=False)
    is_teacher = models.BooleanField('Is Teacher',default=False)
    is_student = models.BooleanField('Is Student', default=False)
    object = CustomUserManager()


# class User(AbstractUser):
#     is_admin = models.BooleanField('Is admin',default=False)
#     is_teacher = models.BooleanField('Is Teacher',default=False)
#     is_student = models.BooleanField('Is Student', default=False)

class Teacher_Image_Upload(models.Model):
    TImage = models.ImageField(upload_to='Teacher__Upload_Images')

class Student_Image_Upload(models.Model):
    SImage = models.ImageField(upload_to='Student__Upload_Images')