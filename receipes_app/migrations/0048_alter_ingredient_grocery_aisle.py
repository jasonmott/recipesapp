# Generated by Django 3.2.9 on 2021-11-13 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_app', '0047_auto_20211113_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='grocery_aisle',
            field=models.CharField(blank=True, choices=[('Baking', 'Baking'), ('Health Foods', 'Health Foods'), ('Spices and Seasonings', 'Spices and Seasonings'), ('Pasta and Rice', 'Pasta and Rice'), ('Bakery/Bread', 'Bakery/Bread'), ('Refrigerated', 'Refrigerated'), ('Canned and Jarred', 'Canned and Jarred'), ('Frozen', 'Frozen'), ('Nut butters, Jams, and Honey', 'Nut butters, Jams, and Honey'), ('Oil, Vinegar, Salad Dressing', 'Oil, Vinegar, Salad Dressing'), ('Condiments', 'Condiments'), ('Savory Snacks', 'Savory Snacks'), ('Milk, Eggs, Other Dairy', 'Milk, Eggs, Other Dairy'), ('Ethnic Foods', 'Ethnic Foods'), ('Tea and Coffee', 'Tea and Coffee'), ('Meat', 'Meat'), ('Gourmet', 'Gourmet'), ('Sweet Snacks', 'Sweet Snacks'), ('Gluten Free', 'Gluten Free'), ('Alcoholic Beverages', 'Alcoholic Beverages'), ('Cereal', 'Cereal'), ('Nuts', 'Nuts'), ('Beverages', 'Beverages'), ('Produce', 'Produce'), ('Not in Grocery Store/Homemade', 'Not in Grocery Store/Homemade'), ('Seafood', 'Seafood'), ('Cheese', 'Cheese'), ('Dried Fruits', 'Dried Fruits'), ('Online', 'Online'), ('Grilling Supplies', 'Grilling Supplies'), ('Bread', 'Bread')], default=None, max_length=100, null=True),
        ),
    ]