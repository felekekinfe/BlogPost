# Generated by Django 4.2.3 on 2023-11-05 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0004_remove_catagory_name_alter_post_catagory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="catagory",
        ),
    ]
