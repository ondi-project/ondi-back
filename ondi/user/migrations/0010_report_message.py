# Generated by Django 3.1.6 on 2021-02-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20210204_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='message',
            field=models.TextField(default='fraud', max_length=255),
            preserve_default=False,
        ),
    ]
