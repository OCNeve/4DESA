# Generated by Django 5.0.1 on 2024-02-06 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_comments_value_posts_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='videos',
            old_name='post_id',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, unique=True),
        ),
    ]
