# Generated by Django 3.0 on 2022-03-26 15:06

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20220325_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amnesities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amneties', models.CharField(choices=[('Essentials', 'Essentials'), ('Wifi', 'Wifi'), ('TV', 'TV'), ('Heat', 'Heat')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.CharField(choices=[('Studio', 'Studio'), ('Ordinary', 'Ordinary'), ('Officetel', 'Officetel'), ('Penthouse', 'Penthouse')], max_length=255, null=True)),
                ('guests', models.IntegerField(default=0, null=True)),
                ('beds', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('street_address', models.CharField(max_length=255, null=True)),
                ('Access_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='Access_code',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='amneties',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='country',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='street_address',
        ),
    ]
