from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import Video_form,ImageForm,DocumentsForm
from .models import Video,Image,Documents

def index(request):
    all_video=Video.objects.all()
    all_image=Image.objects.all()
    all_doc=Documents.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST,files=request.FILES)
        formim =ImageForm(data=request.POST,files=request.FILES)
        formdoc = DocumentsForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        elif formim.is_valid():
            formim.save()
            return HttpResponseRedirect(reverse('index'))
        elif formdoc.is_valid():
            formdoc.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = Video_form()
        formim = ImageForm()
        formdoc = DocumentsForm()
    return render(request,'basic_app/index.html',{'form':form,'formim':formim,'formdoc':formdoc,'all':all_video,'obj':all_image,'alldoc':all_doc})




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in")

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

             user = user_form.save()
             user.set_password(user.password)
             user.save()

             profile = profile_form.save(commit=False)
             profile.user = user

             if 'profile_pic' in request.FILES:
                 profile.profile_pic = request.FILES['profile_pic']


             profile.save()

             registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):

    if request.method == "POST":
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone trued to login and failed!!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("INVALID LOGIN DETAILS...")

    else:
        return render(request,'basic_app/login.html',{})
