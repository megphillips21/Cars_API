# Generated by Django 4.0.5 on 2022-07-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealership',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
