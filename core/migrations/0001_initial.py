# Generated by Django 2.0.3 on 2018-04-08 21:49

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', markdownx.models.MarkdownxField()),
                ('summary', markdownx.models.MarkdownxField()),
                ('cover_image_url', models.URLField()),
            ],
        ),
    ]
