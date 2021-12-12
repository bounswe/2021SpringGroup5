# Generated by Django 3.2.9 on 2021-12-12 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('applicant_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('pathToBadgeImage', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BadgeOfferedByEventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BadgeOwnedByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('isGivenBySystem', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentCommentActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=300)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('pathToEquipmentPostImage', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentPostActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='EventCommentActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=300)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('date_time', models.DateTimeField()),
                ('participant_limit', models.IntegerField()),
                ('spectator_limit', models.IntegerField()),
                ('rule', models.TextField(max_length=300)),
                ('equipment_requirement', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(max_length=10)),
                ('capacity', models.CharField(max_length=25)),
                ('location_requirement', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_info', models.CharField(blank=True, max_length=50, null=True)),
                ('pathToEventImage', models.URLField(blank=True, null=True)),
                ('current_player', models.IntegerField(default=0)),
                ('current_spectator', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventPostActivityStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=70, unique=True)),
                ('is_custom', models.BooleanField()),
            ],
        ),
    ]
