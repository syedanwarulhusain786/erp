# Generated by Django 4.2.4 on 2023-12-19 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0025_alter_salesdeliverydetails_final_quantity_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdeliverydetails',
            name='OrderFk',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='accounting.salesquotation'),
            preserve_default=False,
        ),
    ]
