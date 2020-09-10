# Generated by Django 3.0.8 on 2020-09-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20200904_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Final_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_images', models.ImageField(blank=True, upload_to='new_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='words',
            name='final_images',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]