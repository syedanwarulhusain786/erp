# Generated by Django 4.2.4 on 2023-11-16 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_customuser_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePic',
            field=models.ImageField(blank=True, default='product_images/user-1.jpg', null=True, upload_to='product_images/'),
        ),
    ]