# Generated by Django 3.0.8 on 2020-09-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_delete_testimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]