# Generated by Django 3.2.4 on 2021-06-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity', models.TextField(null=True)),
                ('accessibility', models.FloatField(max_length=255, null=True)),
                ('type', models.TextField(null=True)),
                ('participants', models.IntegerField(max_length=10, null=True)),
                ('price', models.FloatField(max_length=255, null=True)),
                ('link', models.TextField(null=True)),
                ('key', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
