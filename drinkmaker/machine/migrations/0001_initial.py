# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 19:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rawingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_number', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(default='Channel', max_length=256)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MachineSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tap_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(default='Channel', max_length=256)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.Channel')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rawingredients.Ingredient')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tap',
            unique_together=set([('channel', 'tap_number')]),
        ),
    ]