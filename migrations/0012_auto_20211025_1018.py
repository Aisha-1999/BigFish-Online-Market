# Generated by Django 3.2.5 on 2021-10-25 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0011_rename_category_product_db_cname'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_db',
            name='ingredients',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recipe_db',
            name='instruction',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product_db',
            name='price',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product_db',
            name='weight',
            field=models.CharField(max_length=50, null=True),
        ),
    ]