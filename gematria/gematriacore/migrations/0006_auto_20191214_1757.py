# Generated by Django 2.0.13 on 2019-12-14 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gematriacore', '0005_auto_20191214_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gematriamethodletterrule',
            name='letter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_numerical_value', to='gematriacore.Letter'),
        ),
    ]