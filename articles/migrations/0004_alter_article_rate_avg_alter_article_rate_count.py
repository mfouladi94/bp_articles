# Generated by Django 4.2.4 on 2023-10-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articlerating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rate_avg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='rate_count',
            field=models.IntegerField(default=0),
        ),
    ]
