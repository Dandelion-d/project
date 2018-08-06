# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=65, unique=True)),
                ('sex', models.BooleanField(default=False)),
                ('icon', models.ImageField(upload_to='icons')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ttsx_users',
            },
        ),
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=255)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table': 'ttsx_users_ticket',
            },
        ),
    ]