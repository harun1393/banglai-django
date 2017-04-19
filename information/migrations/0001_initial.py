# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('education_rate', models.IntegerField()),
                ('population_density', models.IntegerField(blank=True, null=True)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Divisions'),
        ),
    ]
