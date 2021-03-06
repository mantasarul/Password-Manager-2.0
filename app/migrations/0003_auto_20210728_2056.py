# Generated by Django 3.2.5 on 2021-07-28 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20210728_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountemail',
            name='email_user',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accountphone',
            name='phone_user',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
