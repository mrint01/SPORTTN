# Generated by Django 3.2.8 on 2021-11-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211107_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='pass', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]
