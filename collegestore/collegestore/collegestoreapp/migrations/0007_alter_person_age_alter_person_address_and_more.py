# Generated by Django 4.1.3 on 2023-03-18 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegestoreapp', '0006_alter_person_age_alter_person_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegestoreapp.course'),
        ),
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegestoreapp.department'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mail_id',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='material',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='purpose',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
