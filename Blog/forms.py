from tkinter.ttk import Widget
from .models import Post,Comment
from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreatePostForm(forms.ModelForm):
    title = forms.CharField()
    class Meta:
        model = Post
        fields = ['title','content','image','video']


class CreateComment(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields =('name','body')
        widgets = {
        "name":forms.TextInput(attrs={"class":"col-sm-12"}),
        "body":forms.Textarea(attrs={"class":"form-control"}),


        } 
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


