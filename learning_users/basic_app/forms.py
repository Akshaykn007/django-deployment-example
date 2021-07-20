from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from .models import Video,Image,Documents

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):


    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class Video_form(forms.ModelForm):

    class Meta():
        model = Video
        fields = ('caption','video')


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("captionim","image")

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ("captiondoc","docs")
