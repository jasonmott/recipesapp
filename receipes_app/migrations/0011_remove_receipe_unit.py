# Generated by Django 3.2.8 on 2021-10-31 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0010_alter_receipe_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='unit',
        ),
    ]