# Generated by Django 5.0.3 on 2024-03-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(default='maida', max_length=100)),
                ('ingredient_quantity', models.FloatField()),
                ('ingredient_price', models.FloatField()),
                ('ingredient_unit', models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('piece', 'piece'), ('ml', 'ml'), ('liter', 'liter'), ('plate', 'plate')], max_length=50)),
            ],
        ),
    ]
