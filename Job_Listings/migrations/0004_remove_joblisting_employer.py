# Generated by Django 5.1.4 on 2025-01-09 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Listings', '0003_joblisting_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='employer',
        ),
    ]
