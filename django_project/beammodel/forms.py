from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Beam

class MatrixForm(forms.ModelForm):
	class Meta:
		model = Beam
		# fields which are going to be shown
		fields = '__all__'

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		# whenever this form validates this will create a new user
		model = User
		# fields which are going to be shown
		fields = ['username','email']
