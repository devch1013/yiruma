# Generated by Django 3.2.9 on 2022-01-15 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0006_alter_money_pay_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='amount',
            new_name='due',
        ),
    ]
