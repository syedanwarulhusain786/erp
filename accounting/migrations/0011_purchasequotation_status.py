# Generated by Django 4.2.4 on 2023-12-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_alter_purchasequotation_quotation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasequotation',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
