# Generated by Django 2.0.3 on 2018-04-09 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180408_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
