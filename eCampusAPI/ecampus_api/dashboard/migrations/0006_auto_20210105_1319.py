# Generated by Django 3.1.4 on 2021-01-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210105_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]