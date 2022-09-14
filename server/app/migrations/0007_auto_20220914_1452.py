# Generated by Django 2.2.28 on 2022-09-14 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20220914_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appcomment',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='appseminarparticipant',
            old_name='seminar_id',
            new_name='seminar',
        ),
        migrations.RenameField(
            model_name='appseminarparticipant',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='appseminar',
            name='author_id',
        ),
        migrations.AddField(
            model_name='appseminar',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
