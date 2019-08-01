from django.shortcuts import render,redirect
from .form import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from accounts.form import UserUpdateForm

def register(request):

    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()

            return redirect('profile')
    else:
        form=UserRegisterForm()
    return render(request,"Register.html",{'form':form})



@login_required
def profile(request):

    return render(request,'profile.html')


def about(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm()
    return render(request, 'about.html', {'form' : form})
