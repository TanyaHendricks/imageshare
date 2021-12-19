# Generated by Django 3.2.9 on 2021-11-22 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AddField(
            model_name='image',
            name='album_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to='photos.album'),
            preserve_default=False,
        ),
    ]