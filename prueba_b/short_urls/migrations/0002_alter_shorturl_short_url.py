# Generated by Django 5.0.3 on 2024-03-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
