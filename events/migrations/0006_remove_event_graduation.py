# Generated by Django 2.1.2 on 2018-11-27 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181127_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='graduation',
        ),
    ]
