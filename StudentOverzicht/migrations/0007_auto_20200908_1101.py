# Generated by Django 3.1.1 on 2020-09-08 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentOverzicht', '0006_auto_20200908_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blok',
            old_name='blok',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='voornaam',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='toets',
            old_name='toets',
            new_name='name',
        ),
    ]
