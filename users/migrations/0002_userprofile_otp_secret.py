# Generated by Django 5.1.4 on 2025-03-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp_secret',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
