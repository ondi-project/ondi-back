# Generated by Django 3.1.6 on 2021-02-04 07:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='01029938652', max_length=11, validators=[django.core.validators.MinLengthValidator(11)]),
            preserve_default=False,
        ),
    ]
