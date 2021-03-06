import hashlib
import os
import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from AXF.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods, User, Cart

# 加密
from projectAXF import settings


def genarate_password(param):
    sha = hashlib.sha256()
    sha.update(param.encode('utf-8'))
    return sha.hexdigest()


def home(request):  # 首页
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    # 商品部分
    shopList = Shop.objects.all()
    shophead = shopList[0]
    shoptab = shopList[1:3]
    shopclass = shopList[3:7]
    shopcommend = shopList[7:11]

    # 商品主体内容
    mainshows = MainShow.objects.all()
    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass': shopclass,
        'shopcommend': shopcommend,
        'mainshows': mainshows
    }
    return render(request, 'home/home.html', context=data)


def market(request, childid, sortid):  # 闪购超市
    foodtypes = Foodtypes.objects.all()
    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    # 根据分类下标 获取 对应 分类ID
    categoryid = foodtypes[typeIndex].typeid
    # 子类信息
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames
    # 将每个子类拆分出来
    childTypleList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir1 = {
            'childname': arr[0],  # 子类名称
            'childid': arr[1]  # 子类ID
        }
        childTypleList.append(dir1)

    if childid == '0':  # 全部分类
        goodsList = Goods.objects.filter(categoryid=categoryid)
    else:  # 分类 下 子类
        goodsList = Goods.objects.filter(categoryid=categoryid, childcid=childid)
        # 排序
    if sortid == '1':  # 销量排序
        goodsList = goodsList.order_by('-productnum')
    elif sortid == '2':  # 价格最低
        goodsList = goodsList.order_by('price')
    elif sortid == '3':  # 价格最高
        goodsList = goodsList.order_by(('-price'))
    # 购物车数据
    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user)
    data = {
        'foodtypes': foodtypes,
        'goodsList': goodsList,
        'childTypleList': childTypleList,
        'childid': childid,
        'carts': carts
    }
    return render(request, 'market/market.html', context=data)


def cart(request):  # 购物车
    token = request.session.get('token')
    if token: #有用户显示购物车信息
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)
        return render(request,'cart/cart.html',context={'carts': carts})
    else:
        return render(request, 'cart/cart.html')

def mine(request):  # 我的
    token = request.session.get('token')
    responseData = {}
    if token:  # 登录
        user = User.objects.get(token=token)
        responseData = {
            'name': user.name,
            'rank': user.rank,
            'img': '/static/uploads/' + user.img,
            'isLogin': 1
        }
    else:  # 未登录
        responseData = {
            'img': '/static/uploads/axf.png'
        }
    return render(request, 'mine/mine.html', context=responseData)


def registe(request):
    if request.method == 'GET':
        return render(request, 'mine/registe.html')
    elif request.method == 'POST':
        user = User()
        user.account = request.POST.get('account')
        user.password = genarate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')
        user.addr = request.POST.get('addr')
        file = request.FILES.get('icon')
        filename = user.account + file.name
        user.img = filename
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filepath, 'wb') as fp:
            for data in file.chunks():
                fp.write(data)
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        user.save()
        request.session['token'] = user.token
    return redirect('axf:mine')


def checkaccount(request):
    account = request.GET.get('account')
    responseData = {
        'msg': '账号可用',
        'status': 1  # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(account=account)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)

    except:
        return JsonResponse(responseData)

def checkphone(request):
    phone = request.GET.get('phone')
    print(phone,111)
    responseData = {
        'msg': '手机号可用',
        'status': 1  # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(phone=phone)
        responseData['msg'] = '该手机已注册'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            user = User.objects.get(account=account)
            if user.password == genarate_password(password):    # 登录成功
                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('axf:mine')
            else:   # 登录失败
                return render(request, 'mine/login.html', context={'passwdErr': '密码错误!'})
        except:
            return render(request, 'mine/login.html', context={'acountErr':'账号不存在!'})


def addcart(request):
    goodsid = request.GET.get('goodsid')
    token = request.session.get('token')
    responseData = {
        'msg': '添加到购车',
        'status':1, # 1标识添加成功,0标识添加失败,-1标识未登录
    }
    if token:  # 已登录直接操作模型
        # 获取用户
        user = User.objects.get(token=token)
        # 获取商品
        goods = Goods.objects.get(pk=goodsid)
        # 商品已经存在购物车,只修改商品数量
        # 商品不在购物车,新建对象(加入一条新的数据
        carts = Cart.objects.filter(user=user,goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number + 1
            cart.save()
            responseData['number'] = cart.number
        else:
            cart = Cart()
            cart.goods = goods
            cart.user = user
            cart.number = 1
            cart.save()
            responseData['number'] = cart.number
        return JsonResponse(responseData)
    else:
        responseData['msg'] = '未登录,请登录后操作'
        responseData['status'] = -1
        return JsonResponse(responseData)


def subcart(request):
    # 获取数据
    token = request.session.get('token')
    goodsid = request.GET.get('goodsid')
    # 过滤数据 获取对应用户的数据
    user = User.objects.get(token=token)
    goods = Goods.objects.get(pk=goodsid)
    # 删操作
    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.number = cart.number - 1
    cart.save()
    responseData = {
        'msg': '购物车减操作成功',
        'status': 1,
        'number': cart.number
    }
    return JsonResponse(responseData)


def changecartselect(request):
    isselect = request.GET.get('isselect')
    if isselect == 'true':
        isselect = True
    else:
        isselect = False
    token = request.session.get('token')
    user = User.objects.get(token=token)
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        cart.isselect = isselect
        cart.save()
    return JsonResponse({'msg':'反选操作成功', 'status':1})

def changecartstatus(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()
    responseData = {
        'msg': '选中状态改变',
        'status': 1,
        'isselect': cart.isselect
    }
    return JsonResponse(responseData)
