# Generated by Django 5.0.7 on 2024-08-13 16:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=1000, unique=True)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('meal_type', models.CharField(choices=[('starters', 'Starters'), ('salads', 'Salads'), ('main_dishes', 'Main Dishes'), ('desserts', 'Desserts')], max_length=1000)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Unavailable')], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
