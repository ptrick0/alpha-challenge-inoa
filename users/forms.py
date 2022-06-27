from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1' ,'password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    def __init__(self, *args, **kwargs):
        super(UserPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm New Password"