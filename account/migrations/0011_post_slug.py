# Generated by Django 4.0.5 on 2022-08-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_post_duration_remove_post_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]