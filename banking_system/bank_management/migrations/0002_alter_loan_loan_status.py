# Generated by Django 3.2.18 on 2023-03-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(max_length=15),
        ),
    ]
