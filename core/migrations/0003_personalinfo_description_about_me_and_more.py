# Generated by Django 5.1.2 on 2024-11-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_personalinfo_web_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='description_about_me',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='what_i_do',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='freelance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='web_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
