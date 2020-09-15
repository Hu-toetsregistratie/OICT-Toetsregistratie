# Generated by Django 3.1.1 on 2020-09-08 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentOverzicht', '0004_auto_20200908_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cijfer',
            name='toets',
        ),
        migrations.AddField(
            model_name='cijfer',
            name='toets',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='StudentOverzicht.toets'),
        ),
    ]