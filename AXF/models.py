from django.db import models

# Create your models here.

class Base(models.Model):
    img = models.CharField(max_length=100)  # 图片
    name = models.CharField(max_length=180)  # 名称
    trackid = models.CharField(max_length=10)  # 商品编号

    class Meta:
        abstract = True  # 抽象化
# 轮播
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'  # 修改表名
# 导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'
# 每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

# 商品部分
# 商品部分
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

# 商品主体内容
class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'
# 商品分类
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8)  # 分类ID
    typename = models.CharField(max_length=100)  # 分类名称
    childtypenames = models.CharField(max_length=256)   # 子类名称
    typesort = models.IntegerField()    # 显示先后顺序
    class Meta:
        db_table = 'axf_foodtypes'