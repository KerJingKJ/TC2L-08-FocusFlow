import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0005_mood_created_at_mood_user_alter_mood_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='mood',
            field=models.CharField(choices=[('😊', 'Happy'), ('😐', 'Neutral'), ('😢', 'Sad'), ('😠', 'Angry'), ('😡', 'Furious')], max_length=2),
        ),
        migrations.CreateModel(
            name='MoodHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateField(auto_now_add=True)),
                ('history_notes', models.TextField(blank=True)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.mood')),
            ],
        ),
        migrations.CreateModel(
            name='MoodTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_date', models.DateField(auto_now_add=True)),
                ('tracking_notes', models.TextField(blank=True)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mood.mood')),
            ],
        ),
    ]
