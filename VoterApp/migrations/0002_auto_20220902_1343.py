# Generated by Django 3.2.15 on 2022-09-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VoterApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='candidate_name',
            new_name='candidate_id',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='username',
            new_name='userid',
        ),
    ]
