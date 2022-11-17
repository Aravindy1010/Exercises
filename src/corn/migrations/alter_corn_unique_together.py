from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "add_timestamp_fields"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="corn",
            unique_together={("year",)},
        ),
    ]
