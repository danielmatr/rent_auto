# Generated by Django 3.1 on 2022-02-03 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220203_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
        migrations.AlterField(
            model_name='rating',
            name='ip',
            field=models.CharField(max_length=15, verbose_name='IP адрес'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='main.autopost', verbose_name='фильм'),
        ),
        migrations.AlterField(
            model_name='ratingstar',
            name='value',
            field=models.SmallIntegerField(default=0, verbose_name='Значение'),
        ),
    ]
