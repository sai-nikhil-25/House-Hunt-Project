# Generated by Django 5.0.3 on 2024-03-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtor', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('category', models.CharField(choices=[('DAY', 'Dayton'), ('CNG', 'Cincinnati'), ('CMH', 'Columbus'), ('MCE', 'Mason')], max_length=5)),
                ('photo_main', models.ImageField(upload_to='product')),
                ('photo_1', models.ImageField(blank=True, upload_to='product')),
                ('photo_2', models.ImageField(blank=True, upload_to='product')),
                ('photo_3', models.ImageField(blank=True, upload_to='product')),
                ('photo_4', models.ImageField(blank=True, upload_to='product')),
                ('photo_5', models.ImageField(blank=True, upload_to='product')),
                ('photo_6', models.ImageField(blank=True, upload_to='product')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
