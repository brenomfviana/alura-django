# Generated by Django 4.0.6 on 2022-08-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("code", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=100)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("B", "Basic"),
                            ("I", "Intermediate"),
                            ("A", "Advanced"),
                        ],
                        default="B",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=30)),
                ("cpf", models.CharField(max_length=11)),
                ("birthdate", models.DateField()),
            ],
        ),
    ]
