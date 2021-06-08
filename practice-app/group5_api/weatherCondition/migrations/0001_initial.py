# Generated by Django 3.2.3 on 2021-06-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=15)),
                ('town', models.CharField(max_length=15)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('description', models.CharField(max_length=50)),
                ('degrees', models.FloatField()),
                ('pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('speed', models.FloatField()),
                ('degreeOfWind', models.FloatField()),
            ],
        ),
    ]
