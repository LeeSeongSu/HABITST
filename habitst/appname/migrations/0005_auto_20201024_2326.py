# Generated by Django 3.1.2 on 2020-10-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0004_auto_20201024_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='introduce',
            new_name='introducemyself',
        ),
    ]
