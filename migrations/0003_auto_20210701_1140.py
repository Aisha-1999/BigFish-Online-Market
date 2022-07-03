# Generated by Django 2.0 on 2021-07-01 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_categorydb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorydb',
            old_name='dryfish',
            new_name='categoryname',
        ),
        migrations.RemoveField(
            model_name='categorydb',
            name='freshwater',
        ),
        migrations.RemoveField(
            model_name='categorydb',
            name='seafish',
        ),
        migrations.AddField(
            model_name='categorydb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]