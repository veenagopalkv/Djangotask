# Generated by Django 4.1.3 on 2023-03-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegestoreapp', '0005_alter_person_gender_alter_person_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='Date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='person',
            name='mail_id',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='material',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='purpose',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]