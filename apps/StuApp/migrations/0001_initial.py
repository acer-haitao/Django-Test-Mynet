# Generated by Django 2.0 on 2018-01-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TabName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.IntegerField(max_length=5)),
                ('TabName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='URLDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num', models.IntegerField(max_length=5)),
                ('Name', models.CharField(max_length=100)),
                ('URL', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=100)),
            ],
        ),
    ]