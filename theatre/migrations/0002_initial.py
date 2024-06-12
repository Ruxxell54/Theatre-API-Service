# Generated by Django 4.2.5 on 2024-06-13 01:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("theatre", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="play",
            name="actors",
            field=models.ManyToManyField(blank=True, to="theatre.actor"),
        ),
        migrations.AddField(
            model_name="play",
            name="genres",
            field=models.ManyToManyField(blank=True, to="theatre.genre"),
        ),
        migrations.AddField(
            model_name="performance",
            name="play",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="theatre.play"
            ),
        ),
        migrations.AddField(
            model_name="performance",
            name="theatre_hall",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="theatre.theatrehall"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("performance", "row", "seat")},
        ),
    ]