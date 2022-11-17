from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("weather", "initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="statistics",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="statistics",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="weather",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="weather",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
