# Generated by Django 4.2 on 2023-11-05 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(max_length=1000, null=True, upload_to='images/'),
        ),
    ]
