# Generated by Django 5.0.3 on 2024-03-29 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='realtor',
            new_name='owner',
        ),
    ]
