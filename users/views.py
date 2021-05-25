from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,"users/signup.html",{'form' : form})

@login_required()
def profile(request):
    return render(request,"users/profile.html")
