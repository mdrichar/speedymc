# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operand1', models.IntegerField(default=0)),
                ('operand2', models.IntegerField(default=0)),
                ('operator', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elapsed', models.IntegerField(default=0)),
                ('correct_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Factoid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(default=0)),
                ('factor1', models.IntegerField(default=0)),
                ('factor2', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=512)),
                ('binary_facts', models.ManyToManyField(related_name='qsets', to='flash.BinaryFact')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elapsed', models.IntegerField(default=0)),
                ('binary_fact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash.BinaryFact')),
                ('bout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash.Bout')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='bout',
            name='question_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash.QuestionSet'),
        ),
        migrations.AddField(
            model_name='bout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash.User'),
        ),
    ]
