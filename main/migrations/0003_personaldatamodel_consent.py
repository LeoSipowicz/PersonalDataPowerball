# Generated by Django 4.0.3 on 2022-11-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_mymodel_personaldatamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldatamodel',
            name='consent',
            field=models.CharField(default='I agree', max_length=7),
            preserve_default=False,
        ),
    ]