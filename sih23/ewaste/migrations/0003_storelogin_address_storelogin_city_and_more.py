# Generated by Django 4.2.4 on 2023-10-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewaste', '0002_rename_password_storelogin_ownerpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='storelogin',
            name='address',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='storelogin',
            name='city',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='storelogin',
            name='district',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='storelogin',
            name='shopno',
            field=models.CharField(default='', max_length=100),
        ),
    ]
