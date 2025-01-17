# Generated by Django 3.1.2 on 2020-11-06 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blok', models.CharField(default='', max_length=45)),
                ('jaar', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(default='', max_length=10)),
                ('achternaam', models.CharField(default='', max_length=10)),
                ('student_nummer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Toets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toets_code', models.CharField(default='', max_length=45)),
                ('toets_naam', models.CharField(default='', max_length=45)),
                ('jaar', models.IntegerField(default=0)),
                ('volgorde', models.IntegerField(default=1)),
                ('blok', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Main.blok')),
            ],
        ),
        migrations.CreateModel(
            name='Cijfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voldoende', models.BooleanField(default=False)),
                ('datum_toets', models.CharField(default='00-00-2020', max_length=10)),
                ('blok', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Main.blok')),
                ('student', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Main.student')),
                ('toets_code', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='toetsCode', to='Main.toets')),
                ('toets_naam', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Main.toets')),
            ],
        ),
    ]
