# Generated by Django 3.0.4 on 2020-05-18 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20200518_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='shippAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grocery.Shipping'),
        ),
    ]
