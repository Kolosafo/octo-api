# Generated by Django 4.1.7 on 2024-04-25 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_subject_lessonobject_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonobject',
            name='lesson_id',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
