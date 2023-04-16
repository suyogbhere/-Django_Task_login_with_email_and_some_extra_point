from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='Confirm password(Again)')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields= ('first_name','email','password1','password2','mobile','is_admin','is_teacher'
                 ,'is_student')
        

class Teacher_Image_Upload_form(forms.Form):
    TImage = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),label='Image_Upload')


class Student_Image_Upload_form(forms.Form):
    SImage = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),label='Image_Upload')