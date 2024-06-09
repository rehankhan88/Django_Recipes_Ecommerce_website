# Generated by Django 5.0.6 on 2024-06-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Receipe",
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
                ("receipe_name", models.CharField(max_length=100)),
                ("receipe_description", models.TextField()),
                ("receipe_image", models.ImageField(upload_to="receipe")),
            ],
        ),
    ]
