# Generated by Django 2.1.3 on 2019-03-12 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('move', '0007_auto_20190311_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=255, verbose_name='资源名称')),
                ('rdirector', models.CharField(max_length=255, verbose_name='导演')),
                ('screenwriter', models.CharField(max_length=255, verbose_name='编剧')),
                ('actor', models.CharField(max_length=255, verbose_name='演员')),
                ('language', models.CharField(max_length=255, verbose_name='语言')),
                ('time', models.DateField(verbose_name='上映时间')),
                ('length', models.IntegerField(verbose_name='片长')),
                ('othername', models.CharField(max_length=200, verbose_name='其他名字')),
                ('score', models.FloatField(verbose_name='评分')),
                ('issuperme', models.BooleanField(default=False, verbose_name='是否精选')),
                ('restype', models.CharField(choices=[('MV', '电影'), ('TV', '电视剧')], max_length=255, verbose_name='资源类型')),
                ('picture', models.FileField(null=True, upload_to='media', verbose_name='海报')),
                ('context', models.TextField(null=True, verbose_name='请输入资源的简介')),
                ('ptype', models.CharField(max_length=255, verbose_name='清晰程度')),
                ('purl', models.CharField(max_length=255, null=True, verbose_name='播放地址')),
                ('pname', models.CharField(max_length=255, null=True, verbose_name='分集地址')),
                ('mtype', models.CharField(choices=[('XIGUA', '西瓜视频'), ('JIJI', '吉吉影音'), ('ONLINE', '在线播放')], max_length=100, verbose_name='播放方式')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='move.Area', verbose_name='产地')),
                ('catalog', models.ManyToManyField(to='move.Cata', verbose_name='影片类型')),
                ('pmov', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='move.NormalUser', verbose_name='视频文件')),
            ],
        ),
    ]
