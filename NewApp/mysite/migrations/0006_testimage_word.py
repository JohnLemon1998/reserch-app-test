# Generated by Django 3.0.8 on 2020-08-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200828_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimage',
            name='word',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]