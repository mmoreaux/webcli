# Generated by Django 4.1 on 2022-08-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0002_command_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
