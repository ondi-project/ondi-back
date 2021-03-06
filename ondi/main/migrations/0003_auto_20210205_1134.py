# Generated by Django 3.1.6 on 2021-02-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210205_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveproduct',
            name='l_sprice',
            field=models.IntegerField(default=0, verbose_name='라이브 시작가격'),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(upload_to='', verbose_name='대표사진'),
        ),
    ]
