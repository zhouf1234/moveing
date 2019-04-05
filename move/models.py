from django.db import models

# Create your models here.

#地区
class Area(models.Model):
    aname = models.CharField(max_length=255, verbose_name="地区")


# 类型
class Cata(models.Model):
    cname = models.CharField(max_length=255, verbose_name="类型名称")
    cremark = models.TextField(verbose_name="备注")


# 电影电视资源
# class Resource(models.Model):
#     # 这里定义一个元组，可以进行选择类型
#     RESTYPE_CHOICE = (
#         ('MV', '电影'),
#         ('TV', '电视剧'),
#     )
#
#     RESTYPE_CH = (
#         ('XIGUA', '西瓜视频'),
#         ('JIJI', '吉吉影音'),
#         ('ONLINE', '在线播放'),
#     )
#
#     rname = models.CharField(max_length=255, verbose_name="资源名称")
#     rdirector = models.CharField(max_length=255, verbose_name="导演")
#     screenwriter = models.CharField(max_length=255, verbose_name="编剧")
#     actor = models.CharField(max_length=255, verbose_name="演员")
#     area = models.ForeignKey('Area', on_delete=models.CASCADE, verbose_name="产地")
#     language = models.CharField(max_length=255, verbose_name="语言")
#     time = models.DateField(verbose_name="上映时间")
#     length = models.IntegerField(verbose_name="片长")
#     othername = models.CharField(max_length=200, verbose_name="其他名字")
#     score = models.FloatField(verbose_name="评分")
#     issuperme = models.BooleanField(default=False, verbose_name="是否精选")
#     restype = models.CharField(choices=RESTYPE_CHOICE, max_length=255, verbose_name="资源类型")
#     picture = models.FileField("海报", upload_to='media', null=True)  # 图片地址
#     context = models.TextField("请输入资源的简介", null=True)
#     catalog = models.ManyToManyField(to='Cata', verbose_name="影片类型")
#
#     ptype = models.CharField(max_length=255, verbose_name="清晰程度")
#     purl = models.CharField(max_length=255, verbose_name="播放地址",null=True)
#     pname = models.CharField(max_length=255, verbose_name="分集地址",null=True)
#     mtype = models.CharField(choices=RESTYPE_CH, max_length=100, verbose_name="播放方式")
#
#     pmov = models.OneToOneField(to='NormalUser', verbose_name="视频文件",on_delete=models.CASCADE,null=True)

#主要用来上传各类文件用的功能，见views
class NormalUser(models.Model):
    username=models.CharField('用户名',max_length=30)
    #用户名
    headImg=models.FileField('文件',upload_to='media')#文件名







