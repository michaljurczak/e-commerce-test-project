from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from .forms import MJStoreUserCreationForm
from mjstore_main.decorators import unauthenticated_user
from mjstore_main.models import Customer
# Create your views here.


@unauthenticated_user
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_view')
    return render(request, 'mjstore_main/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('main_view')


@unauthenticated_user
def register_view(request):
    context = {'form': MJStoreUserCreationForm}
    if request.method == "POST":
        form = MJStoreUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    return render(request, 'mjstore_main/register.html', context)
