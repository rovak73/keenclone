# Generated by Django 3.0.8 on 2020-08-16 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0003_remove_specialty_user'),
        ('profiles', '0008_auto_20200813_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='specialties.Specialty'),
        ),
    ]
