# Generated by Django 3.1 on 2022-02-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentauto',
            old_name='renter',
            new_name='user',
        ),
        migrations.AddField(
            model_name='rentauto',
            name='info',
            field=models.TextField(default='Bishkek'),
        ),
    ]
