# Generated by Django 3.1.2 on 2020-11-02 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toets',
            name='blok',
        ),
        migrations.AddField(
            model_name='toets',
            name='blok',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Main.blok'),
        ),
    ]
