from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Beam

class MatrixForm(forms.ModelForm):
	class Meta:
		model = Beam
		# fields which are going to be shown
		fields = '__all__'