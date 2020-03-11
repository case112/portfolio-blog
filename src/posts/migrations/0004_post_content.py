# Generated by Django 2.2.7 on 2019-11-27 15:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=21),
            preserve_default=False,
        ),
    ]
