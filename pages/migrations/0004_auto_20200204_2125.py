# Generated by Django 3.0.2 on 2020-02-04 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200203_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='seo_description',
            field=models.TextField(blank=True, default=None, help_text='Small description about this page.', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='seo_keywords',
            field=models.CharField(blank=True, default=None, help_text='eg: keyword1, keyword2, keyword3 ...', max_length=512, null=True),
        ),
    ]