# Generated by Django 3.0 on 2020-11-05 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RS69Eapp', '0003_producttrafficip'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RS69Eapp.Shipping'),
        ),
    ]
