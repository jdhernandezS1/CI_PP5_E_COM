# Generated by Django 3.2.16 on 2023-02-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payup', '0005_order_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.CharField(max_length=30),
        ),
    ]