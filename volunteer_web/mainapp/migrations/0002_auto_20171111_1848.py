# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'applied'), (2, 'approved'), (3, 'unapproved'), (4, 'finished')], default=1)),
                ('written_info', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student_job',
            name='job',
        ),
        migrations.RemoveField(
            model_name='student_job',
            name='student',
        ),
        migrations.AlterField(
            model_name='job',
            name='additional_info',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Student_job',
        ),
        migrations.AddField(
            model_name='studentjob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Job'),
        ),
        migrations.AddField(
            model_name='studentjob',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Student'),
        ),
    ]