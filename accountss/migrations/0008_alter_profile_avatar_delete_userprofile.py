<<<<<<< HEAD
# Generated by Django 5.1 on 2024-09-22 14:59
=======
# Generated by Django 5.1 on 2024-09-19 14:30
>>>>>>> 2b8346cdd6f6c8f1d244b01f4a3b93046bef082d

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountss', '0007_merge_20240918_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
<<<<<<< HEAD
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
=======
            field=models.ImageField(blank=True, upload_to='avatar'),
>>>>>>> 2b8346cdd6f6c8f1d244b01f4a3b93046bef082d
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
