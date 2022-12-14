from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "corn_unique_on_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="corn",
            name="corn_yield",
            field=models.IntegerField(
                help_text="Corn grain yield in the United States (measured in 1000s of megatons)"
            ),
        ),
        migrations.AlterField(
            model_name="corn",
            name="year",
            field=models.PositiveSmallIntegerField(
                help_text="Year of the harvest", unique=True
            ),
        ),
    ]
