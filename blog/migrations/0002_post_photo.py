# Generated by Django 2.2.3 on 2022-02-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='cars'),
        ),
    ]
