# Generated by Django 4.1.3 on 2024-01-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
    ]
