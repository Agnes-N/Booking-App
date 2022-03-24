# Generated by Django 3.0 on 2022-03-26 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20220326_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='apartment',
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='myApp.Location'),
        ),
    ]