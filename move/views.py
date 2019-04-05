from django.shortcuts import render,redirect,HttpResponse
import json
from django.http import JsonResponse
from . models import Area,Cata,NormalUser

# Create your views here.

#登录
def login(request):
    if request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        if user=='evev'and pwd=='123456':           #后台管理员
            request.session['k1']=user
            return redirect('/index/')
        else:
            error = '用户名或密码错误！请重新输入！'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

#登录进去之后的主页面显示的
def index(request):
    value = request.session.get('k1')
    return render(request, 'index.html',{'value':value})

#地区展示
def AreList(request):
    are = Area.objects.all()
    context = {'are':are}
    return render(request, 'are.html',context=context)

#类型展示
def CateList(request):
    cate = Cata.objects.all()
    context = {'cate':cate}
    return render(request, 'cate.html',context=context)

# 资源添加--获取新页面
def addRes(request):
    are = Area.objects.all()
    cate = Cata.objects.all()
    context = {
             'are': are,
             'cate':cate,
            }
    return render(request,'add_res.html',context=context)

#资源添加，上传数据
def updateRes(request):
    #获取data的数据
    data = request.POST.get('data', None)
    data = json.loads(data)
    print(data)
    rimage = request.FILES.get("picture",None)
    rmove = request.FILES.get("pmove", None)    #读取不到路径，文件也无法读取，得到的只是文件标题
    print(rimage,rmove)

    # Resource.objects.create(
    #     rname = data['rname'],
    #     rdirector=data['rdirector'],
    #     screenwriter=data['screenwriter'],
    #     actor=data['actor'],
    #     area_id=data['area'],
    #     language=data['language'],
    #     time=data['time'],
    #     length=data['length'],
    #     othername=data['othername'],
    #     score=data['score'],
    #     issuperme=data['issuperme'],
    #     restype=data['restype'],
    #     context=data['context'],
    #     ptype=data['ptype'],
    #     purl=data['purl'],
    #     pname=data['pname'],
    #     mtype=data['mtype'],
    #     picture=rimage,
    #     pmove=rmove
    # )
    # Resource.objects.get(rname=data['rname']).catalog.add(data['catalog'])

    return JsonResponse({
        'status': 'success',
        'message': '创建成功',
        'info': ''
    })

#此处专为上传各类文件写的一个按钮--word、excel、pdf、图片、mp4视频都已成功上传
from django import forms
class NormalUserForm(forms.Form):
    #form的定义和model类的定义很像
    username=forms.CharField()
    headImg=forms.FileField()

def fileU(request):
    if request.method == "POST":
        uf = NormalUserForm(request.POST, request.FILES)  # 刚显示时，实例化表单（是否有数据）
        if uf.is_valid():  # 验证数据是否合法，当合法时可以使用cleaned_data属性。
            # 用来得到经过'clean'格式化的数据，会所提交过来的数据转化成合适的Python的类型。
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            # write in database
            normalUser = NormalUser()  # 实例化NormalUser对象
            normalUser.username = username
            normalUser.headImg = headImg
            normalUser.save()  # 保存到数据库表中
            return HttpResponse('Upload Succeed!上传成功！')  # 重定向显示内容（跳转后内容）
    else:
        uf = NormalUserForm()  # 刚显示时，实例化空表单
    return render(request, 'file_u.html', {'uf': uf})  # 只有刚显示时才起作用
