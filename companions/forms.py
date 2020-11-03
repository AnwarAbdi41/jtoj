from django import forms
from datetime import datetime
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .models import UserProfileModel
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
    #specify date from 1960 to 2019
NUM_YEARS = [x for x in range(1960, 2019)]

class UserLogin(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ('profile_picture', 'date_of_birth')


