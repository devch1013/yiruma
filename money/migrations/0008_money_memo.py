# Generated by Django 3.2.9 on 2022-02-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0007_rename_amount_money_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
