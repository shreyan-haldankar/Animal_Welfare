# Generated by Django 4.1 on 2022-09-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('card_name', models.CharField(max_length=100)),
                ('card_number', models.IntegerField()),
                ('exp_month', models.CharField(max_length=50)),
                ('exp_year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('donationAmount', models.IntegerField()),
            ],
        ),
    ]