# Generated by Django 3.0.3 on 2020-03-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtransport', '0003_auto_20200314_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='contact_data',
            field=models.CharField(blank=True, default=0, max_length=100),
            preserve_default=False,
        ),
    ]
