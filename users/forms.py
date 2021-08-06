from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from .models import User, Feedback


def avatar_file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('The avatar file is too big, please limit it to 2M')


class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(min_length=1,max_length=20,required=False,
                               error_messages={
                                   'min_length': 'Nickname must be at least 4 characters',
                                   'min_length': 'Nickname cannot be more than 20 characters',
                               },
                               widget=forms.TextInput())
    avatar = forms.ImageField(required=False, validators=[avatar_file_size],
                              widget=forms.FileInput(attrs={'class' : 'n'}))
    email = forms.EmailField(required=False,
                             error_messages={
                                 'invalid': 'Please enter a valid email address',
                             },
                             widget=forms.EmailInput())
    gender = forms.CharField(min_length=1,max_length=1,required=False,
                             widget=forms.HiddenInput())
    mobile = forms.CharField(min_length=11,max_length=11,required=False,
                             error_messages={
                                 'min_length': 'Please enter an 11-digit mobile phone number',
                                 'max_length': 'Please enter an 7-digit mobile phone number',
                             },
                             widget=forms.NumberInput())

    class Meta:
        model = User
        fields = ['nickname', 'avatar', 'email', 'gender', 'mobile']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=4,max_length=15,
                               error_messages={
                                   'min_length': 'Username must be at least 4 characters',
                                   'max_length': 'Username cannot be more than 15 characters',
                                   'required': 'Username can not be empty',
                               },
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter your user name here'}))
    password = forms.CharField(min_length=8,max_length=15,
                               error_messages={
                                   'min_length': 'Password must be no less than 8 characters',
                                   'max_length': 'Password cannot be more than 15 characters',
                                   'required': 'password can not be blank',
                               },
                               widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password here'}))

    class Meta:
        model = User
        fields = ['username', 'password']

    error_messages = {'invalid_login': 'Wrong user name or password', }


class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=4,max_length=15,
                               error_messages={
                                   'min_length': 'User name cannot be less than 4 characters',
                                   'max_length': 'User name cannot be more than 15 characters',
                                   'required': 'Username can not be empty',
                               },
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter your user name'}))
    password1 = forms.CharField(min_length=8, max_length=15,
                                error_messages={
                                    'min_length': 'Password must be no less than 8 characters',
                                    'max_length': 'Password cannot be more than 15 characters',
                                    'required': 'Password can not be blank',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'}))
    password2 = forms.CharField(min_length=8,max_length=15,
                                error_messages={
                                    'min_length': 'Password must be no less than 8 characters',
                                    'max_length': 'Password cannot be more than 15 characters',
                                    'required': 'Password can not be blank',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please confirm your password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    error_messages = {'password_mismatch': 'The two passwords are inconsistent', }


class ChangePwdForm(PasswordChangeForm):
    old_password = forms.CharField(error_messages={'required': 'Cannot be empty',},
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the previous password'})
    )
    new_password1 = forms.CharField(error_messages={'required': 'Cannot be empty',},
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the new password'})
    )
    new_password2 = forms.CharField(error_messages={'required': 'Cannot be empty',},
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the confirmed password'})
    )
