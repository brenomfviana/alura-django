# Generated by Django 4.0.6 on 2022-07-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipe_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
