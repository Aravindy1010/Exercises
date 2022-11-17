from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "weather_float_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statistics",
            name="avg_max_temp",
            field=models.FloatField(
                help_text="Average of the daily max temperatures recorded (measured in degrees Celsius)",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="statistics",
            name="avg_min_temp",
            field=models.FloatField(
                help_text="Average of the daily min temperatures recorded (measured in degrees Celsius)",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="statistics",
            name="station_id",
            field=models.CharField(
                help_text="Weather station identifier", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="statistics",
            name="total_precipitation",
            field=models.FloatField(
                help_text="Sum of the daily precipitation recorded (measured in centimeters)",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="statistics",
            name="year",
            field=models.PositiveSmallIntegerField(
                help_text="Year that the statistics were calculated for"
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="date",
            field=models.DateField(help_text="Date of data collection"),
        ),
        migrations.AlterField(
            model_name="weather",
            name="max_temp",
            field=models.FloatField(
                help_text="Highest temperature recorded for the day (measured in degrees Celsius)"
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="min_temp",
            field=models.FloatField(
                help_text="Lowest temperature recorded for the day (measured in degrees Celsius)"
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="precipitation",
            field=models.FloatField(
                help_text="Amount of precipitation recorded for the day (measured in centimeters)"
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="station_id",
            field=models.CharField(
                help_text="Weather station identifier", max_length=50
            ),
        ),
    ]
