# Generated by Django 3.0.8 on 2020-07-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
