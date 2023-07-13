# Generated by Django 4.2.3 on 2023-07-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('overall_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('coffee_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('food_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('vibe_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('wifi_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('quiet_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('meeting_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('study_work_rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
