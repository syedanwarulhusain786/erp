# Generated by Django 4.2.4 on 2023-11-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(max_length=255, unique=True)),
                ('ledger_type', models.CharField(max_length=50)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('current_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
    ]