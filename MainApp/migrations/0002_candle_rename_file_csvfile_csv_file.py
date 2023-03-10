# Generated by Django 4.1.6 on 2023-02-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Candle",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("open", models.FloatField()),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("close", models.FloatField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name="csvfile", old_name="file", new_name="csv_file",
        ),
    ]
