# Generated by Django 3.0.2 on 2020-02-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_menuitem_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='path',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='type',
            field=models.IntegerField(choices=[(1, 'link'), (2, 'page')], default=1),
        ),
    ]