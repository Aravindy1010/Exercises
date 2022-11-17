from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "add_timestamp_fields"),
    ]
    operations = [
        migrations.AlterField(
            model_name="weather",
            name="max_temp",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="weather",
            name="min_temp",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="weather",
            name="precipitation",
            field=models.FloatField(),
        ),
    ]
