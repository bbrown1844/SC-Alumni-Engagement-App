# Generated by Django 2.1.2 on 2018-11-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20181127_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='grad',
        ),
        migrations.AddField(
            model_name='event',
            name='graduation',
            field=models.CharField(default='', max_length=50),
        ),
    ]