# Generated by Django 3.0.6 on 2020-05-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeForm', '0015_auto_20200520_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_model',
            name='password',
            field=models.CharField(default='flksjf', max_length=50),
        ),
    ]