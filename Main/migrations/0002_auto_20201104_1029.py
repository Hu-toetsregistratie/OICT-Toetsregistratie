# Generated by Django 3.1.2 on 2020-11-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cijfer',
            name='datum_toets',
            field=models.CharField(default='00-00-2020', max_length=10),
        ),
    ]
