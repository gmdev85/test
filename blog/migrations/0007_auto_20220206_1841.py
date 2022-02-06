# Generated by Django 2.2.3 on 2022-02-06 17:41

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220206_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_de',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]