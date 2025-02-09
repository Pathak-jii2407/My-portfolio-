# Generated by Django 5.0.6 on 2024-07-04 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projects",
            old_name="project",
            new_name="project_file",
        ),
        migrations.AddField(
            model_name="projects",
            name="project_name",
            field=models.CharField(
                default=datetime.datetime(
                    2024, 7, 4, 23, 13, 31, 685579, tzinfo=datetime.timezone.utc
                ),
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="survey",
            name="rating",
            field=models.IntegerField(
                choices=[(1, "1 - cry"), (2, "2 - serious"), (3, "3 - happy")]
            ),
        ),
    ]
