from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "alter_corn_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="corn",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="corn",
            name="year",
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
