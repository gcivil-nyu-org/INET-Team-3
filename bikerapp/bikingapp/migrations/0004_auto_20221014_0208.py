# Generated by Django 2.2 on 2022-10-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikingapp', '0003_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
