# Generated by Django 4.2.4 on 2023-11-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='name',
            field=models.CharField(choices=[('CEO', 'CEO'), ('HR_MANAGER', 'HR Manager'), ('HR_HEAD', 'HR Head'), ('ACCOUNTANT', 'Accountant'), ('USER', 'User'), ('HEAD', 'Head'), ('MANAGER', 'MANAGER'), ('VIEWER', 'View')], max_length=50, unique=True),
        ),
    ]