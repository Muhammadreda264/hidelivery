# Generated by Django 3.0.8 on 2020-07-29 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_auto_20200728_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='logo',
        ),
    ]
