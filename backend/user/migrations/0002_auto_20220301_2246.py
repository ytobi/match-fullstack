# Generated by Django 3.1.1 on 2022-03-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deposit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')], help_text="Role must be one of ['Buyer', 'Seller']", max_length=225),
        ),
    ]