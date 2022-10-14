# Generated by Django 2.2 on 2022-10-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(verbose_name='event date and time')),
                ('date_created', models.DateTimeField(verbose_name='event created date')),
                ('public_private', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
