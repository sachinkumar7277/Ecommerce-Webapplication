# Generated by Django 3.0.4 on 2020-05-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_auto_20200516_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
