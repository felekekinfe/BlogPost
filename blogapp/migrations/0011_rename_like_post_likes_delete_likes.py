# Generated by Django 4.2.3 on 2023-11-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0010_post_like"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="like",
            new_name="likes",
        ),
        migrations.DeleteModel(
            name="Likes",
        ),
    ]
