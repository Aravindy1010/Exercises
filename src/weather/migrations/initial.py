from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Statistics",
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
                ("station_id", models.CharField(max_length=50)),
                ("year", models.PositiveSmallIntegerField()),
                ("avg_max_temp", models.FloatField(null=True)),
                ("avg_min_temp", models.FloatField(null=True)),
                ("total_precipitation", models.FloatField(null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Weather",
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
                ("station_id", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("max_temp", models.DecimalField(decimal_places=1, max_digits=4)),
                ("min_temp", models.DecimalField(decimal_places=1, max_digits=4)),
                ("precipitation", models.DecimalField(decimal_places=1, max_digits=4)),
            ],
            options={
                "unique_together": {
                    ("station_id", "date", "max_temp", "min_temp", "precipitation")
                },
            },
        ),
    ]
