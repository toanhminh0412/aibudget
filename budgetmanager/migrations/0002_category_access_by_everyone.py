# Generated by Django 4.2.2 on 2023-12-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='access_by_everyone',
            field=models.BooleanField(default=False),
        ),
    ]
