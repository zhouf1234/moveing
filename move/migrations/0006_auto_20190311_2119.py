# Generated by Django 2.1.3 on 2019-03-11 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('move', '0005_normaluser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='pmove',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='move.NormalUser', verbose_name='视频文件'),
        ),
    ]
