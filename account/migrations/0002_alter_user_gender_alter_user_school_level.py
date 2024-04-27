# Generated by Django 4.1.7 on 2024-04-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('prefer not to say', 'prefer not to say')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='school_level',
            field=models.CharField(blank=True, choices=[('high school', 'high school'), ('middle school', 'middle school')], max_length=200, null=True),
        ),
    ]
