# Generated by Django 4.1.7 on 2024-04-26 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_lessonobject_lesson_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessondetails',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
