from django.shortcuts import render

# Create your views here.
from AXF.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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


def market(request,categoryid):  # 闪购超市
    foodtypes = Foodtypes.objects.all()
    goodsList = Goods.objects.filter(categoryid=categoryid)
    data = {
        'foodtypes': foodtypes,
        'goodsList': goodsList
    }
    return render(request, 'market/market.html',context=data)


def cart(request):  # 购物车
    return render(request, 'cart/cart.html')


def mine(request):  # 我的
    return render(request, 'mine/mine.html')
