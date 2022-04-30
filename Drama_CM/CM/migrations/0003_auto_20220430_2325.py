# Generated by Django 3.0.8 on 2022-04-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0002_auto_20220430_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='DRAMA',
            fields=[
                ('drama_name', models.CharField(max_length=30, unique=True, verbose_name='드라마 제목')),
                ('drama_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='드라마 아이디')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='watched_drama',
            field=models.TextField(default=''),
        ),
    ]
