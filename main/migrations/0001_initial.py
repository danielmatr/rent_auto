# Generated by Django 3.1 on 2022-02-02 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('year', models.PositiveSmallIntegerField(default=2015)),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('soon', 'Скоро')], max_length=20)),
                ('kpp', models.CharField(choices=[('mechanics', 'Механика'), ('auto', 'Автомат')], max_length=20)),
                ('text', models.TextField(default='Ogon mawina')),
                ('prices', models.PositiveSmallIntegerField(default=4000)),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Auto',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AutoPostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.autopost')),
            ],
        ),
        migrations.AddField(
            model_name='autopost',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='main.category'),
        ),
    ]
