from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserAuthenticationForm, UserPasswordForm
from django.contrib import messages

def custom_login(request):
    form_login = UserAuthenticationForm()

    if request.user.is_authenticated:
        return redirect('list_tickers')

    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login successfully')
            return redirect('list_tickers')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Login')

    return render(request, 'users/login.html', { 'form_login': form_login })

def custom_register(request):
    form_register = UserForm()

    if request.method == 'POST':
        form_register = UserForm(request.POST)
        
        if form_register.is_valid():
            form_register.save()
            username = form_register.cleaned_data.get('username')
            raw_password = form_register.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Registration successful')
            return redirect('login')

    return render(request, 'users/new.html', {'form_register': form_register})

@login_required
def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('list_tickers')

@login_required
def change_password(request):
    if request.method == "POST":
        form_passw = UserPasswordForm(request.user, request.POST)
        if form_passw.is_valid():
            user = form_passw.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Password changed sucessfully')
            return redirect('list_tickers')
    else:
        form_passw = UserPasswordForm(request.user)
    return render(request, 'users/change.html', {'form_passw': form_passw})