# Generated by Django 2.1.2 on 2018-11-27 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.TextField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('numberAttendees', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('p', 'Pending'), ('a', 'Approved')], default='a', max_length=1)),
                ('host_first_name', models.CharField(default='', max_length=50)),
                ('host_last_name', models.CharField(default='', max_length=50)),
                ('host_grad', models.CharField(default='', max_length=50)),
                ('host_major', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('class_year', models.CharField(max_length=4)),
                ('checkedIn', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='event', to='events.Person'),
        ),
    ]
