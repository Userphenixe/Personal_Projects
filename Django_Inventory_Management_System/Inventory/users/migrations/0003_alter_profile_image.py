# Generated by Django 5.1.2 on 2024-11-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='Default.png', null=True, upload_to='profile_images/'),
        ),
    ]
