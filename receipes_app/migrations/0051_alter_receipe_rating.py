# Generated by Django 3.2.9 on 2021-11-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0050_receipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
