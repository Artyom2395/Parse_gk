from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['url']


class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "validate",  "placeholder": "Введите имя пользователя",
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "validate",  "placeholder": "Введите пароль",
    }), error_messages={
        'required': 'Пароль обязателен для заполнения',
        'min_length': 'Пароль должен содержать не менее 8 символов',
    })
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "validate",  "placeholder": "Подтвердите пароль",
    }), error_messages={
        'required': 'Подтверждение пароля обязательно для заполнения',
        'min_length': 'Пароль должен содержать не менее 8 символов',
    })

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']