# Generated by Django 4.0.3 on 2022-11-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_personaldatamodel_emaillistconsent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldatamodel',
            name='emailListConsent',
            field=models.BooleanField(default=False),
        ),
    ]