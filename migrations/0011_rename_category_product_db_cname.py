# Generated by Django 3.2.5 on 2021-09-17 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0010_rename_name_category_db_cname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_db',
            old_name='category',
            new_name='cname',
        ),
    ]
