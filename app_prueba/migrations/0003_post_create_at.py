# Generated by Django 4.2.3 on 2023-07-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prueba', '0002_remove_post_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_at',
            field=models.CharField(default='2010-03-01', max_length=20, verbose_name='creado'),
            preserve_default=False,
        ),
    ]
