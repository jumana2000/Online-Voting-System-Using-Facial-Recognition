# Generated by Django 3.2.15 on 2022-09-02 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dashboard', '0001_initial'),
        ('Accounts', '0002_alter_voterregister_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=20)),
                ('candidate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.candidateregister')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.voterregister')),
            ],
        ),
    ]
