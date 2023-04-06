# Generated by Django 3.2.18 on 2023-04-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_authentication', '0002_auto_20230328_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.CharField(choices=[('graduated', 'Graduate'), ('not_graduated', 'Not Graduate')], default=('graduated', 'Graduate'), max_length=13),
        ),
        migrations.AlterField(
            model_name='user',
            name='property_area',
            field=models.CharField(choices=[('urban', 'Urban'), ('semi-urban', 'Semiurban'), ('rural', 'Rural')], default=('urban', 'Urban'), max_length=10),
        ),
    ]
