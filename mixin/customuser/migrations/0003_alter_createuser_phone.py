# Generated by Django 4.2.7 on 2023-11-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customuser", "0002_alter_createuser_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createuser",
            name="phone",
            field=models.CharField(max_length=12),
        ),
    ]