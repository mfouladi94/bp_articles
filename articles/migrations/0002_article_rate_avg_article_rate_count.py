# Generated by Django 4.2.4 on 2023-10-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rate_avg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='rate_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]