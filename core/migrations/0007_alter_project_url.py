# Generated by Django 5.1.2 on 2024-11-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_onlinecourse_description_onlinecourse_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
