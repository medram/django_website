# Generated by Django 3.0.2 on 2020-02-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200210_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
    ]
