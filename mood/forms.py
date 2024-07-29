from django import forms
from mood.models import *


class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'journal_entry']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields =  ['first_name', 'last_name', 'username', 'profile_image','email', 'password']

class LoginForm(forms.Form):
   username = forms.CharField(max_length=100, required=True)
   password = forms.CharField(widget=forms.PasswordInput, required=True)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'first_name', 'last_name', 'email']