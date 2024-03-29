# Generated by Django 4.2.4 on 2023-10-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='storelogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=250)),
                ('shopno', models.CharField(default='', max_length=100)),
                ('address', models.TextField(default='', max_length=1000)),
                ('city', models.CharField(default='', max_length=250)),
                ('district', models.CharField(default='', max_length=250)),
                ('pincode', models.CharField(default='', max_length=10)),
                ('contact', models.CharField(default='', max_length=10)),
                ('ownerfirstname', models.CharField(max_length=250)),
                ('ownersecondname', models.CharField(max_length=250)),
                ('ownerusername', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('ownerpassword', models.CharField(max_length=250)),
                ('confirmpass', models.CharField(max_length=250)),
            ],
        ),
    ]
