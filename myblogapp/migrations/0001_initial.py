# Generated by Django 2.2.3 on 2019-07-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msgboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('message', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Msgboard',
            },
        ),
    ]
