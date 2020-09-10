# Generated by Django 3.0.8 on 2020-09-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_karuta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karuta_data',
            name='mistake_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Final_Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.User')),
            ],
        ),
    ]