# Generated by Django 3.2.15 on 2022-08-30 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VoterApp', '0003_userregister_dob'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]