from django import forms
from django.contrib.auth.models import User
from .models import Teacher,Student,Principal,Question
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class TeacherForm(forms.ModelForm):
	# email=forms.EmailField()	
	# level=forms.IntegerField(default=1)
	# mobile_no=forms.IntegerField(max_length=10)
	# class_id=forms.CharField(max_length=2,primary_key=True)
	class Meta():
		model =Teacher
		fields =('email','mobile_no','class_id')

class PrincipalForm(forms.ModelForm):
	# email=forms.EmailField()	
	# level=forms.IntegerField(default=1)
	# mobile_no=forms.IntegerField(max_length=10)
	# class_id=forms.CharField(max_length=2,primary_key=True)
	class Meta():
		model =Principal
		fields =('email','mobile_no')
