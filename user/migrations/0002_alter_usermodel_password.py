# Generated by Django 5.0 on 2024-10-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
