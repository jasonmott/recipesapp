# Generated by Django 3.2.9 on 2021-12-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0066_alter_receipe_ingredient_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='receipe',
            name='tag',
            field=models.ManyToManyField(blank=True, to='receipes_app.Tag'),
        ),
        migrations.AddField(
            model_name='receipe',
            name='dish_type',
            field=models.ManyToManyField(blank=True, to='receipes_app.DishType'),
        ),
    ]
