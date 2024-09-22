from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountss', '0007_merge_20240918_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
