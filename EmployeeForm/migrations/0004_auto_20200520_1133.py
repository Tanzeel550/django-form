# Generated by Django 3.0.6 on 2020-05-20 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeForm', '0003_employee_model_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_model',
            name='birth_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='city',
            field=models.CharField(default='empty', max_length=16),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='email',
            field=models.EmailField(default='myfuck@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='hire_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='hourly_rate',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='social_security',
            field=models.CharField(default='empty', max_length=26),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='state',
            field=models.CharField(default='empty', max_length=16),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='status',
            field=models.CharField(default='empty', max_length=26),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='title',
            field=models.CharField(default='empty', max_length=26),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='worked_before',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee_model',
            name='zip_code',
            field=models.IntegerField(default='92'),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='address',
            field=models.CharField(default='empty', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='name',
            field=models.CharField(default='empty', max_length=26),
        ),
    ]
