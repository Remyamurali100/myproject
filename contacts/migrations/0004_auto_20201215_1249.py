# Generated by Django 3.1.1 on 2020-12-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20201215_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnotification',
            name='receiver',
            field=models.IntegerField(),
        ),
    ]
