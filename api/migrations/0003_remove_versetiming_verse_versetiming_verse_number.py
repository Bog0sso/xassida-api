# Generated by Django 4.1.2 on 2022-10-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_author_slug_reciter_slug_xassida_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="versetiming",
            name="verse",
        ),
        migrations.AddField(
            model_name="versetiming",
            name="verse_number",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
