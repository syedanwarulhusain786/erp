# Generated by Django 4.2.4 on 2023-11-13 23:33

import commonApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0003_delete_unitofmeasurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMaterialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=commonApp.models.get_image_filename)),
                ('product_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonApp.productmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=commonApp.models.get_image_filename)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonApp.product')),
            ],
        ),
    ]
