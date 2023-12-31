# Generated by Django 4.2.4 on 2023-12-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0018_salesquotation_salesitemrow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesquotation',
            name='status',
        ),
        migrations.AlterField(
            model_name='salesquotation',
            name='approval',
            field=models.BooleanField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending'), ('DeliverPending', 'DeliverPending'), ('Completed', 'Completed')], max_length=20),
        ),
    ]
