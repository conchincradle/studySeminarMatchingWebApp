# Generated by Django 2.2.28 on 2022-09-15 03:09

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
            name='AccountUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200, verbose_name='パスワード')),
                ('profile', models.TextField(verbose_name='自己紹介')),
                ('sound_profile', models.CharField(max_length=200, verbose_name='サウンドURL')),
                ('user_icon', models.CharField(max_length=200, verbose_name='アイコンURL')),
                ('birthday', models.DateField(verbose_name='誕生日')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
