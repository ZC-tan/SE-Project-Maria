# Generated by Django 3.2 on 2021-06-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0005_auto_20210612_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='is_recycled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docuser',
            name='is_favourited',
            field=models.BooleanField(default=False),
        ),
    ]
