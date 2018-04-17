# Generated by Django 2.0.4 on 2018-04-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('rut', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField()),
                ('rut', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('height', models.FloatField()),
                ('weight', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('position', models.CharField(choices=[('BA', 'Base'), ('ES', 'Escolta'), ('AL', 'Alero'), ('AP', 'AlaPivot'), ('PI', 'Pivot')], default='BA', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
    ]
