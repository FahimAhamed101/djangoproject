# Generated by Django 4.2.6 on 2023-10-16 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_user_acountant_remove_user_employee_fraud_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, unique=True)),
                ('last_name', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('totaltransaction', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('totalammount', models.IntegerField()),
                ('disputes', models.IntegerField()),
                ('totaldisputesammount', models.IntegerField()),
                ('accceptedtrans', models.IntegerField()),
                ('charbackcountrate', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('limit', models.IntegerField()),
                ('declinetrans', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bin', models.CharField(max_length=100)),
                ('Lastfour', models.CharField(max_length=100)),
                ('ammount', models.IntegerField()),
                ('payout', models.CharField(max_length=100)),
                ('code', models.IntegerField()),
                ('accepted', models.IntegerField()),
                ('InternalTransactionid', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]