# Generated by Django 3.2.4 on 2021-11-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WAMG', '0009_auto_20211113_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='things',
            name='photo',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
