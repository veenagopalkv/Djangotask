# Generated by Django 4.1.3 on 2023-03-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegestoreapp', '0004_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='person',
            name='material',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='purpose',
            field=models.CharField(max_length=20),
        ),
    ]
