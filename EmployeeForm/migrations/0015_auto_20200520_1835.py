# Generated by Django 3.0.6 on 2020-05-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeForm', '0014_remove_employee_model_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_model',
            name='email',
            field=models.EmailField(default='myfuck@gmail.com', max_length=17),
        ),
    ]