# Generated by Django 3.2.16 on 2023-01-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
