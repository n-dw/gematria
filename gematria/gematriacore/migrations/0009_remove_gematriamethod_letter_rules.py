# Generated by Django 2.0.13 on 2019-03-23 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gematriacore', '0008_auto_20190323_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gematriamethod',
            name='letter_rules',
        ),
    ]
