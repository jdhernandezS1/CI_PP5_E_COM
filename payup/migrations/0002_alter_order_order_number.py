# Generated by Django 3.2.16 on 2023-01-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=40),
        ),
    ]
