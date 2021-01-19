# Generated by Django 3.0.7 on 2020-07-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20200711_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='description',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='id',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='song_title',
        ),
        migrations.AddField(
            model_name='songs',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songs',
            name='song_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='songs',
            name='song_name',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]