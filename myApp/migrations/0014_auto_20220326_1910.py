# Generated by Django 3.0 on 2022-03-26 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20220326_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='apartment',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='apartment',
        ),
    ]
