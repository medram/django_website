# Generated by Django 3.0.2 on 2020-02-10 12:54

import classifier.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20200206_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_1',
            field=models.ImageField(blank=True, upload_to=classifier.models._post_image_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_2',
            field=models.ImageField(blank=True, upload_to=classifier.models._post_image_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, upload_to=classifier.models._post_image_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_4',
            field=models.ImageField(blank=True, upload_to=classifier.models._post_image_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_5',
            field=models.ImageField(blank=True, upload_to=classifier.models._post_image_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to=classifier.models._post_image_path),
        ),
    ]
