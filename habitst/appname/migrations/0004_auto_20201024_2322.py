# Generated by Django 3.1.2 on 2020-10-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_auto_20201024_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='introduce',
            field=models.CharField(max_length=50),
        ),
    ]
