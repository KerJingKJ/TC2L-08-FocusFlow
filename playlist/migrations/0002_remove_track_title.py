# Generated by Django 5.1 on 2024-09-05 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='title',
        ),
    ]
