# Generated by Django 3.1.4 on 2020-12-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20201212_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=256),
        ),
    ]
