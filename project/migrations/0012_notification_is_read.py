# Generated by Django 4.2 on 2023-11-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_blog_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]