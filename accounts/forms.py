from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LeaseForm(ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        # exclude = ['user']


class MemberForm0(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['teacher', 'student', 'user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

