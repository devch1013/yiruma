# Generated by Django 3.2.9 on 2021-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentinfo',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('regi_date', models.DateField()),
                ('cancel_date', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('sch_year', models.CharField(choices=[('elem1', '초등학교 1학년'), ('elem2', '초등학교 2학년'), ('elem3', '초등학교 3학년'), ('elem4', '초등학교 4학년'), ('elem5', '초등학교 5학년'), ('elem6', '초등학교 6학년'), ('midd1', '중학교 1학년'), ('midd2', '중학교 2학년'), ('midd3', '중학교 3학년'), ('high1', '고등학교 1학년'), ('high2', '고등학교 2학년'), ('high3', '고등학교 3학년')], default=None, max_length=50, null=True)),
            ],
        ),
    ]
