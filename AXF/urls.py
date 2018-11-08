from django.conf.urls import url

from AXF import views

urlpatterns =[
    url(r'^$', views.home, name='index'),  # 首页
    url(r'^home/$', views.home, name='home'),   # 首页
    url(r'^market/(\d+)/(\d+)/$', views.market, name='market'), # 闪购超市
    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^mine/$', views.mine, name='mine'),   # 我的
    url(r'^registe/$', views.registe, name='registe'),  # 注册
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'), # 账号验证
    url(r'^logout/$', views.logout, name='logout'), # 退出
    url(r'^login/$', views.login, name='login'),    # 登录
    url(r'^checkphone/$',views.checkphone,name='checkphone'), # 手机号验证
    url(r'addcart/$',views.addcart,name='addcart'), # 购物车加操作
    url(r'^subcart/$',views.subcart,name='subcart'), # 购物车减操作
    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'), # 修改选中状态
    url(r'changecartselect/$', views.changecartselect,name='changecartselect'), # 全选/取消全选
]
