# Generated by Django 2.2.3 on 2019-09-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_auto_20190916_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_item',
            name='count',
            field=models.IntegerField(),
        ),
    ]
