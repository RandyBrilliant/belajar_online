from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.
def RegisterPage(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully created your account!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})