# Generated by Django 4.1.5 on 2023-08-12 01:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(choices=[('tashkent', 'tashkent'), ('tashkent reg', 'tashkent reg'), ('andijan', 'andijan'), ('namangan', 'namangan'), ('fergana', 'fergana'), ('sirdarya', 'sirdarya'), ('jizzakh', 'jizzakh'), ('samarkand', 'samarkand'), ('surkhandarya', 'surkhandarya'), ('kashkadarya', 'kashkadarya'), ('navoiy', 'navoiy'), ('bukhara', 'bukhara'), ('kharezm', 'kharezm'), ('karakalpakistan', 'karakalpakistan')], default='tashkent', max_length=25)),
                ('auth_step', models.CharField(choices=[('first step', 'first step'), ('second step', 'second step')], default='first step', max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
