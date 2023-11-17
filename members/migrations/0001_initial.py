# Generated by Django 4.2.3 on 2023-11-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pasta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("title_tag", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
