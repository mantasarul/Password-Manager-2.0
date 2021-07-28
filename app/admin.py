from django.contrib import admin
from .models import AccountEmail, AccountPhone, Account

# Register your models here.
# Admin panel username: root
# Admin panel password: 6******

class EmailModel(admin.ModelAdmin):
    list_display = ['email']


class PhoneModel(admin.ModelAdmin):
    list_display = ['phone']


class AccountModel(admin.ModelAdmin):
    list_display = [
        'category',
        'url',
        'username',
        'password',
        'email_id',
        'phone_id',
        'recovery_code'
    ]


admin.site.register(AccountEmail, EmailModel)
admin.site.register(AccountPhone, PhoneModel)
admin.site.register(Account, AccountModel)