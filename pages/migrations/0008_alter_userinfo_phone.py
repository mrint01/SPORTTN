# Generated by Django 3.2.7 on 2021-11-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20211129_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
