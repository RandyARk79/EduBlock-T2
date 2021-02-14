# Generated by Django 3.1.6 on 2021-02-14 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='post',
            name='data_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]