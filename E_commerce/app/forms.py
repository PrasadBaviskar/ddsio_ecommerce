from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username=forms.EmailField()
    class Meta():
        model = User
        fields = ('username','password')
        labels = {'username':'Email'}
