# Generated by Django 4.2.4 on 2023-08-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_user_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absentie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(max_length=30)),
                ('dat', models.DateField(null=True)),
            ],
        ),
    ]
