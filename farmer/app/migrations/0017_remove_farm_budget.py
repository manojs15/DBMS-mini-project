# Generated by Django 5.0.2 on 2024-03-09 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_farm_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='budget',
        ),
    ]
