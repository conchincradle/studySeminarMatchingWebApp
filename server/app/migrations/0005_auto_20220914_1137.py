# Generated by Django 2.2.28 on 2022-09-14 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220914_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appcomment',
            old_name='posted_id',
            new_name='posted',
        ),
    ]
