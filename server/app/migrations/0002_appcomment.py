# Generated by Django 2.2.28 on 2022-09-13 07:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='コメント内容')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.AccountUser')),
                ('posted_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post')),
            ],
        ),
    ]
