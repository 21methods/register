from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib import messages


# Create your views here.

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '@username', 'min_length': '5'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',  'password1', 'password2']
        help_text = {
            'username': '',
            'password1': '',
            'password2': '',
        }


def welcome(request):
    return render(request, 'authentication/welcome.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password )
            login(request, user)
            message.success(request,'registered successful!')


            # Redirect to a success page or login the user
            return redirect('authentication/login')
    else:
        form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

'''
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        user = User.object.create_user(username,email,password)
        user.save|()

        messages.success(request,"your account is created successfully!")
        return redirect ('login')
    return render(request, 'authentication/register.html', {"form":loginform()})
    '''

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']

        User = authenticate(username=username, password=password)

        if User is not None:
            login(request, user)
            return render(request, 'authentication/home.html', {'first_name' : first_name})

        else:
            messages.error(request, 'Bad Credentials!')
            return redirect('login')


    return render(request, 'authentication/login.html')

@login_required(login_url="/login")
def home(request):
    return render(request, 'authentication/home.html')
