# Generated by Django 4.2.4 on 2023-12-12 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_per_piece', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('calculation_unit', models.CharField(choices=[('Piece', 'Piece'), ('Liter', 'Liter'), ('Meter', 'Meter'), ('Centimeter', 'Centimeter')], default='Piece', max_length=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonApp.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commonApp.product')),
            ],
        ),
    ]
