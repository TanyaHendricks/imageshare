# Generated by Django 3.2.9 on 2021-11-22 02:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]