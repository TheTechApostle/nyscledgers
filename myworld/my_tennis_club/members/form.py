from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class corpReg(forms.ModelForm):
	class Meta:
		model = CorpRegister
		fields = "__all__"


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email','username','password1','password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

# class attendance(forms.ModelForm):
# 	class Meta:
# 		model = attendance
# 		fields = "__all__"


class DocumentFile(forms.ModelForm):
	class Meta:
		model = document
		fields = '__all__'


# forms.py



class CSVImportForm(forms.Form):
    csv_file = forms.FileField()


class CSVImportFormPPA(forms.Form):
    csv_file = forms.FileField()


class mycdsfetch(forms.Form):
	mycds = forms.CharField(max_length=20, label="fetch by CDS")


