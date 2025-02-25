# Generated by Django 5.0.3 on 2024-03-31 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0008_alter_bookappointment_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp.customer')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp.listing')),
            ],
        ),
    ]
