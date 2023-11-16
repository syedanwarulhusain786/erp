# Generated by Django 4.2.4 on 2023-11-13 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_itemrow_remove_quotation_bank_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='discount',
            new_name='final_amt',
        ),
        migrations.AddField(
            model_name='quotation',
            name='sub_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='tax_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]