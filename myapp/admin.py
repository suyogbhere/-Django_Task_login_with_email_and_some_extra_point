from django.contrib import admin
from.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','email','mobile','is_admin','is_teacher','is_student']

@admin.register(Teacher_Image_Upload)
class TeacherPhotoAdmin(admin.ModelAdmin):
    list_display=['TImage']


@admin.register(Student_Image_Upload)
class TeacherPhotoAdmin(admin.ModelAdmin):
    list_display=['SImage']