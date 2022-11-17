from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "alter_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weather",
            name="max_temp",
            field=models.FloatField(
                default=-9999,
                help_text="Highest temperature recorded for the day (measured in degrees Celsius)",
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="min_temp",
            field=models.FloatField(
                default=-9999,
                help_text="Lowest temperature recorded for the day (measured in degrees Celsius)",
            ),
        ),
        migrations.AlterField(
            model_name="weather",
            name="precipitation",
            field=models.FloatField(
                default=-9999,
                help_text="Amount of precipitation recorded for the day (measured in centimeters)",
            ),
        ),
    ]
