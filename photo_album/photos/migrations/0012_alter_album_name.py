# Generated by Django 3.2.9 on 2021-11-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_auto_20211122_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(default='Unknown', max_length=20, unique=True),
        ),
    ]
