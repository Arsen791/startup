# Generated by Django 4.1.2 on 2023-10-25 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0004_blog_average_rating_blog_total_ratings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='total_ratings',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='total_score',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
