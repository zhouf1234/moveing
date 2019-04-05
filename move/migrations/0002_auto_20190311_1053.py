# Generated by Django 2.1.3 on 2019-03-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('move', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerlist',
            name='pmove',
            field=models.FileField(null=True, upload_to='media', verbose_name='视频'),
        ),
        migrations.AlterField(
            model_name='playerlist',
            name='pname',
            field=models.CharField(max_length=255, null=True, verbose_name='分集地址'),
        ),
        migrations.AlterField(
            model_name='playerlist',
            name='purl',
            field=models.CharField(max_length=255, null=True, verbose_name='播放地址'),
        ),
    ]
