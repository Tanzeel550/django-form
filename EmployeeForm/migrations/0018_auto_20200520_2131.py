# Generated by Django 3.0.6 on 2020-05-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeForm', '0017_auto_20200520_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_model',
            name='social_security',
            field=models.CharField(default='empty', max_length=26),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='gender',
            field=models.CharField(default='male', max_length=7),
        ),
    ]