# Generated by Django 3.2.9 on 2021-12-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0069_alter_receipe_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='image_URL',
            field=models.URLField(blank=True, null=True),
        ),
    ]