# Generated by Django 4.1.5 on 2023-01-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=63, null=True, verbose_name='Имя'),
        ),
    ]