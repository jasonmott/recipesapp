# Generated by Django 3.2.9 on 2021-11-13 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0054_ingredientamount_receipe1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='receipe1',
            new_name='orig_receipe',
        ),
    ]