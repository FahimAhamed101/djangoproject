# Generated by Django 4.2.6 on 2023-10-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_userinfo_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]