from django.db import models

# Create your models here.

class Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name_plural = "Emails"


class Phone(models.Model):
    phone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.phone}"

    class Meta:
        verbose_name_plural = "Phones"


class Account(models.Model):
    category = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=500)
    email_id = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, blank=True)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True)
    recovery_code = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.category} {self.url} {self.username} {self.password} {self.email_id} {self.phone_id} {self.recovery_code} "

    class Meta:
        verbose_name_plural = "Accounts"