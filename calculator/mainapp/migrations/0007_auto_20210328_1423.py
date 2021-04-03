# Generated by Django 3.1.7 on 2021-03-28 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_grade_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='fromF',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]