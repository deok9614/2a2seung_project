# Generated by Django 4.2.5 on 2023-09-18 01:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("topic", models.CharField(default="전체", max_length=255)),
                ("publish", models.CharField(default="Y", max_length=1)),
                ("views", models.IntegerField(default=0)),
                ("author_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date modified"
                    ),
                ),
            ],
        ),
    ]
