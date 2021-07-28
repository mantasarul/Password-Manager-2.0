from app.models import Account, AccountPhone, AccountEmail
from django import forms

class EmailForm(forms.ModelForm):
    model = AccountEmail
    fields = ['email']

class PhoneForm(forms.ModelForm):
    model = AccountPhone
    fields = ['phone']

class AccountForm(forms.ModelForm):
    model = Account
    fields = [
        'category',
        'url',
        'username',
        'password',
        'email_id',
        'phone_id',
        'recovery_code'
    ]
    labels = {
        'category': 'Category',
        'url': 'URL',
        'username': 'Username',
        'password': 'Password',
        'email_id': 'Email',
        'phone_id': 'Phone',
        'recovery_code': 'Recovery Codes',
    }