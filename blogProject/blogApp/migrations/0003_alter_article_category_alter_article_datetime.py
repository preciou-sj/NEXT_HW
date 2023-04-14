# Generated by Django 4.1.7 on 2023-04-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_article_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]