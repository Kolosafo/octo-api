# Generated by Django 4.1.7 on 2024-04-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_quicklearn'),
    ]

    operations = [
        migrations.AddField(
            model_name='quicklearn',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
