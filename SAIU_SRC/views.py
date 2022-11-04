from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, "info.html")