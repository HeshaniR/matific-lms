# Generated by Django 3.2.8 on 2021-10-10 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='score',
        ),
    ]