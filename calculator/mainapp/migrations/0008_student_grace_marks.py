# Generated by Django 3.1.7 on 2021-05-09 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210328_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grace_marks',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
