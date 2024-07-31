# Generated by Django 5.0.7 on 2024-07-27 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_alter_publication_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория публикации',
                'verbose_name_plural': 'Категории публикаций',
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Хештег',
                'verbose_name_plural': 'Хештеги',
            },
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='created_date',
        ),
        migrations.AddField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='read_time',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.category'),
        ),
        migrations.AddField(
            model_name='publication',
            name='hashtags',
            field=models.ManyToManyField(null=True, to='journal.hashtag'),
        ),
    ]
