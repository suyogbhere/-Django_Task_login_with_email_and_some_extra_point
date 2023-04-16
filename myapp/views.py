from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from.models import *

# Create your views here.
def index(request):
    
    return render(request,'myapp/home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            msg = 'User Created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        fm = SignupForm()
    return render(request,'myapp/signup.html',{'form':fm, 'msg':msg})


def login_view(request):
    fm = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                msg='Invalid Credentils'
        else:
            msg='error in validating form'
    return render(request,'myapp/login.html',{'form':fm,'msg':msg})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        timage = Teacher_Image_Upload.objects.all()
        simage = Student_Image_Upload.objects.all()
        return render(request,'myapp/dashboard.html',{'timage':timage,'simage':simage})
    else:
        return redirect('login')
    
def Teacher_photo_upload(request):
    msg=None
    if request.method =='POST':
        fm = Teacher_Image_Upload_form(request.POST, request.FILES)
        if fm.is_valid():
            ph = fm.cleaned_data['TImage']
            data = Teacher_Image_Upload(TImage=ph)
            data.save()
            msg='Image Upload successfully!!'
    else:
        fm = Teacher_Image_Upload_form()
    return render(request,'myapp/teacher_photo.html',{'form':fm, 'msg':msg})

def Student_photo_upload(request):
    msg=None
    if request.method =='POST':
        fm = Student_Image_Upload_form(request.POST, request.FILES)
        if fm.is_valid():
            ph = fm.cleaned_data['TImage']
            data = Student_Image_Upload(SImage=ph)
            data.save()
            msg='Image Upload successfully!!'
    else:
        fm = Student_Image_Upload_form()
    return render(request,'myapp/student_photo.html',{'form':fm})

