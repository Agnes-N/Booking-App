# Generated by Django 3.0 on 2022-03-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20220326_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
