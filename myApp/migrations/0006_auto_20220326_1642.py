# Generated by Django 3.0 on 2022-03-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_auto_20220326_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='location',
            new_name='apart_location',
        ),
        migrations.AddField(
            model_name='location',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.Apartment'),
        ),
        migrations.AlterField(
            model_name='location',
            name='street_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
