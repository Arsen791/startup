# Generated by Django 4.2 on 2023-11-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(max_length=1000, null=True, upload_to='files/'),
        ),
    ]
