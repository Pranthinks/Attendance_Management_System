# Generated by Django 4.2.4 on 2023-08-27 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
    ]
