# Generated by Django 5.1.2 on 2024-11-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_skill_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='start_date',
        ),
        migrations.AddField(
            model_name='education',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
