# Generated by Django 3.2.16 on 2022-12-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]