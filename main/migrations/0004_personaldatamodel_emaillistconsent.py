# Generated by Django 4.0.3 on 2022-11-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_personaldatamodel_consent'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldatamodel',
            name='emailListConsent',
            field=models.CharField(blank=True, default=False, max_length=7),
        ),
    ]
