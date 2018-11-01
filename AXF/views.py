from django.shortcuts import render

# Create your views here.
from AXF.models import Wheel, Nav, Mustbuy


def home(request): # 首页
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    data={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys
    }
    return render(request, 'home/home.html',context=data)


def market(request):  # 闪购超市
    return render(request, 'market/market.html')


def cart(request):  # 购物车
    return render(request, 'cart/cart.html')


def mine(request):  # 我的
    return render(request, 'mine/mine.html')