# Generated by Django 3.2.9 on 2021-11-22 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20211122_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album_id',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.RESTRICT, to='photos.album'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
