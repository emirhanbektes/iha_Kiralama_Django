# Generated by Django 5.0.1 on 2024-05-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='product',
            field=models.IntegerField(),
        ),
    ]
