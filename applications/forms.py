import re
from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Division, Email
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Тема письма"}))
    to = forms.CharField(label='Кому', widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': "E-mail получателя"}))

    cc_myself = forms.CharField(label='Копия', required=False, widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Копия"}))

    content = forms.CharField(label='Текст', widget=forms.Textarea(
        attrs={"class": "form-control", 'placeholder': "Тело письма", "rows": 5}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username max 150"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': "Пароль"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username max 150"}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': "email"}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Имя"}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Фамилия"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': "Повторить пароль"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class AddOrder(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'sender_name', 'sender_email', 'datetime_send', 'text_body', 'uid_division']

        widgets = {
            'subject': forms.TextInput(attrs={"class": "form-control"}),
            'sender_name': forms.TextInput(attrs={"class": "form-control"}),
            'sender_email': forms.TextInput(attrs={"class": "form-control"}),
            'datetime_send': forms.DateInput(attrs={"class": "form-control"}),
            'text_body': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),
            'uid_division': forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['datetime_send'].initial = datetime.now()

    def clean_data(self):
        subject = self.cleaned_data['subject']
        if re.match(r'\d', subject):
            raise ValidationError('Название не должно начинатся с цифры')
        return subject


