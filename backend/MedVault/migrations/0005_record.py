# Generated by Django 5.0.4 on 2024-05-06 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedVault', '0004_delete_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.DateField()),
                ('dr_name', models.CharField(max_length=200)),
                ('complaint', models.CharField(max_length=200)),
                ('diagnose', models.CharField(max_length=250)),
                ('prescription', models.TextField()),
                ('hospital_name', models.CharField(max_length=250)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedVault.patient')),
            ],
        ),
    ]