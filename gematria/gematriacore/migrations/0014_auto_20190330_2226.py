# Generated by Django 2.0.13 on 2019-03-30 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gematriacore', '0013_auto_20190330_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordspelling',
            name='word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spelling', to='gematriacore.Word'),
        ),
    ]