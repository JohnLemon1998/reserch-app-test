# Generated by Django 3.0.8 on 2020-08-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
