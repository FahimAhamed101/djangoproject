# Generated by Django 4.2.6 on 2023-10-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
    ]