# Generated by Django 4.2.4 on 2023-12-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0013_remove_purchasequotation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitemrow',
            name='status',
            field=models.CharField(choices=[('ACTIVE', True), ('INACTIVE', False)], max_length=20),
        ),
    ]
