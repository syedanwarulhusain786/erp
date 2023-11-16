# Generated by Django 4.2.4 on 2023-11-10 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('billing_address', models.TextField()),
                ('shipping_address', models.TextField(blank=True)),
                ('quotation_number', models.CharField(max_length=255)),
                ('quotation_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('tax_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255)),
                ('bank_details', models.TextField(blank=True)),
                ('payment_due_date', models.DateField(blank=True, null=True)),
                ('terms_and_conditions', models.TextField(blank=True)),
                ('notes_comments', models.TextField(blank=True)),
                ('validity_accepted_by_customer', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.quotation')),
            ],
        ),
    ]