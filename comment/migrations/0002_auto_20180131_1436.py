# Generated by Django 2.0 on 2018-01-31 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='footer',
            field=models.TextField(),
        ),
    ]
