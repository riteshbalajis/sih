# Generated by Django 4.2.4 on 2023-10-21 16:31

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
                ('ownerfirstname', models.CharField(max_length=250)),
                ('ownersecondname', models.CharField(max_length=250)),
                ('ownerusername', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('confirmpass', models.CharField(max_length=250)),
            ],
        ),
    ]