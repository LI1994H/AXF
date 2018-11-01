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