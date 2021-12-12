# Generated by Django 3.2.9 on 2021-12-12 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpostactivitystream',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpostactivitystream',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='skill_requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.skilllevel'),
        ),
        migrations.AddField(
            model_name='eventpost',
            name='sport_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.sport'),
        ),
        migrations.AddField(
            model_name='eventcommentactivtystream',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventcommentactivtystream',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventcomment'),
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
        migrations.AddField(
            model_name='equipmentpostactivtystream',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipmentpostactivtystream',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.equipmentpost'),
        ),
        migrations.AddField(
            model_name='equipmentpost',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipmentpost',
            name='sport_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.sport'),
        ),
        migrations.AddField(
            model_name='equipmentcommentactivtystream',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipmentcommentactivtystream',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.equipmentcomment'),
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
        migrations.AddField(
            model_name='badgeownedbyuser',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.badge'),
        ),
        migrations.AddField(
            model_name='badgeownedbyuser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='badgeofferedbyeventpost',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.badge'),
        ),
        migrations.AddField(
            model_name='badgeofferedbyeventpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost'),
        ),
        migrations.AddField(
            model_name='application',
            name='event_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.eventpost'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
