# Generated by Django 3.0.8 on 2020-08-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20200827_0605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimage',
            name='image',
        ),
        migrations.AlterField(
            model_name='testimage',
            name='created_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
