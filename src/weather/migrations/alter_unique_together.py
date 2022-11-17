from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "added_help_text"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="statistics",
            unique_together={("station_id", "year")},
        ),
        migrations.AlterUniqueTogether(
            name="weather",
            unique_together={("station_id", "date")},
        ),
    ]
