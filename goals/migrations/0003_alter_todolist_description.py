# Generated by Django 5.1 on 2024-08-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_rename_title_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
