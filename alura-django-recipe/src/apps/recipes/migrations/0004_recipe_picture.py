# Generated by Django 4.0.6 on 2022-07-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_recipe_is_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="picture",
            field=models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d/"),
        ),
    ]