# Generated by Django 5.1.4 on 2025-01-09 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Details', '0006_alter_application_employer'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer', to='employee.employee'),
        ),
    ]
