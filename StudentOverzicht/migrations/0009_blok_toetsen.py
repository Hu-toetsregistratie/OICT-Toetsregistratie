# Generated by Django 3.1.1 on 2020-09-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentOverzicht', '0008_auto_20200908_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='blok',
            name='toetsen',
            field=models.ManyToManyField(to='StudentOverzicht.Toets'),
        ),
    ]