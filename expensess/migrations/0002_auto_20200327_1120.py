# Generated by Django 3.0.2 on 2020-03-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensess',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
