# Generated by Django 3.1.6 on 2021-03-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default='False'),
        ),
    ]
