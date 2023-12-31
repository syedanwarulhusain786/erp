# Generated by Django 4.2.4 on 2023-12-19 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting', '0022_salesdeliverydetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesitemrow',
            name='quantity_left',
            field=models.PositiveIntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesdeliverydetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.salesitemrow'),
        ),
        migrations.AlterField(
            model_name='salesquotation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
