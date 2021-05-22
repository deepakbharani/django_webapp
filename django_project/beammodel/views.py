from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Beam
from .forms import MatrixForm, UserUpdateForm


def input(request):
    form = MatrixForm()
    return render(request, 'beammodel/input.html', {'form': form})

