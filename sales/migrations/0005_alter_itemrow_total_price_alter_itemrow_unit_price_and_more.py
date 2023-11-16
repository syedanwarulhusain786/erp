# Generated by Django 4.2.4 on 2023-11-13 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_rename_discount_quotation_final_amt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrow',
            name='total_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='itemrow',
            name='unit_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='final_amt',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='sub_total',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='tax_total',
            field=models.CharField(max_length=255),
        ),
    ]
