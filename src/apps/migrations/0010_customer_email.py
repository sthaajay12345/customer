# Generated by Django 3.0.8 on 2020-08-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
