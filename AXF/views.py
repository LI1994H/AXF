from django.shortcuts import render

# Create your views here.
from AXF.models import Wheel


def home(request): # 首页
    wheels = Wheel.objects.all()
    data={
        'wheels':wheels,
    }
    return render(request, 'home/home.html',context=data)


def market(request):  # 闪购超市
    return render(request, 'market/market.html')


def cart(request):  # 购物车
    return render(request, 'cart/cart.html')


def mine(request):  # 我的
    return render(request, 'mine/mine.html')