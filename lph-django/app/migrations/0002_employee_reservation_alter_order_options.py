# Generated by Django 4.2.7 on 2023-12-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EMPLOYEEID', models.AutoField(default=901, primary_key=True, serialize=False)),
                ('POSITION', models.CharField(max_length=50, null=True)),
                ('SALARY', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('FIRSTNAME', models.CharField(max_length=50, null=True)),
                ('LASTNAME', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('RESERVATIONID', models.AutoField(default=9001, primary_key=True, serialize=False)),
                ('RESERVATIONDATE', models.DateField()),
                ('RESERVATIONTIME', models.DateTimeField()),
                ('PARTYSIZE', models.IntegerField()),
                ('PREFERENCE', models.CharField(max_length=255)),
                ('CONTACTPHONE', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'reservations',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
    ]
