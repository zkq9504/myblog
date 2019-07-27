# Generated by Django 2.2.3 on 2019-07-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('text', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('abstract', models.CharField(max_length=250)),
                ('href', models.URLField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='Life',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('abstract', models.CharField(max_length=250)),
                ('href', models.URLField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'life',
            },
        ),
        migrations.CreateModel(
            name='Msgboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('message', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'msgboard',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
                ('abstract', models.CharField(max_length=250)),
                ('href', models.URLField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'skill',
            },
        ),
    ]
