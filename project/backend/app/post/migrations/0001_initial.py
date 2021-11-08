# Generated by Django 3.2.9 on 2021-11-08 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
            name='EquipmentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField()),
                ('pathToEquipmentPostImage', models.URLField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('date_time', models.DateTimeField()),
                ('participant_limit', models.IntegerField()),
                ('spectator_limit', models.IntegerField()),
                ('rule', models.TextField(max_length=300)),
                ('equipment_requirement', models.TextField(max_length=300)),
                ('status', models.CharField(max_length=10)),
                ('capacity', models.CharField(max_length=25)),
                ('location_requirement', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_info', models.CharField(blank=True, max_length=50, null=True)),
                ('repeating_frequency', models.IntegerField()),
                ('pathToEventImage', models.URLField(blank=True, null=True)),
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
                ('sport_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventPostActivityStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost')),
            ],
        ),
        migrations.AddField(
            model_name='eventpost',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.skilllevel'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='sport_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.sport'),
        ),
        migrations.CreateModel(
            name='EventCommentActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventcomment')),
            ],
        ),
        migrations.AddField(
            model_name='eventcomment',
            name='event_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.eventpost'),
        ),
        migrations.AddField(
            model_name='eventcomment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EquipmentPostActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.equipmentpost')),
            ],
        ),
        migrations.AddField(
            model_name='equipmentpost',
            name='sport_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.sport'),
        ),
        migrations.CreateModel(
            name='EquipmentCommentActivtyStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.equipmentcomment')),
            ],
        ),
        migrations.AddField(
            model_name='equipmentcomment',
            name='equipment_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.equipmentpost'),
        ),
        migrations.AddField(
            model_name='equipmentcomment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BadgeOwnedByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('isGivenBySystem', models.BooleanField()),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.badge')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BadgeOfferedByEventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.badge')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=8)),
                ('applicant_type', models.CharField(max_length=9)),
                ('event_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='badgeownedbyuser',
            constraint=models.UniqueConstraint(fields=('owner', 'badge'), name='badge owned by a user'),
        ),
        migrations.AddConstraint(
            model_name='badgeofferedbyeventpost',
            constraint=models.UniqueConstraint(fields=('post', 'badge'), name='badge offered by an event post'),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('user', 'event_post'), name='application to an event post per user'),
        ),
    ]
