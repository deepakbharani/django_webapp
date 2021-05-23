from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Beam
from .forms import MatrixForm, UserUpdateForm


def input(request):
    form = MatrixForm()
    return render(request, 'beammodel/input.html', {'form': form})

def mult(request):
	val1 = float(request.GET['mass'])
	val2 = float(request.GET['stiffness'])
	res = val1 * val2

	#messages.success(request, f'Multiplication done and here is your result: {res}')

	return render(request,'beammodel/result.html',{'result':res})