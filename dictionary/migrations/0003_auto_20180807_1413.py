# Generated by Django 2.1 on 2018-08-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20180807_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='dict_remark',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
