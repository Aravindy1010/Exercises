from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="corn",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="corn",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
