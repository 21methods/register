from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages


# Create your views here.
class RegistrationForm(UserCreationForm):
    '''def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'id':'id_username',
            'type': 'text', 
            'placeholder':'username',
            'maxlength':'15',
        })'''
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '@username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
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
            return redirect('home')
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
    return render(request, 'authentication/login.html')

def home(request):
    return render(request, 'authentication/home.html')
