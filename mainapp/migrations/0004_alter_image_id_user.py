# Generated by Django 4.2 on 2023-04-27 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_remove_user_file_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="id_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="mainapp.user",
            ),
        ),
    ]
