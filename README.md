MxShop
-------
项目简介：
-------
MxShop是基于python3.6+Django 1.11.6+Vue+Xadmin开发的前后端分离的生鲜电商项目,支持用户手机注册、短信验证、第三方登录、密码修改以及个人中心的展示；商品列表的分类、排序、筛选，轮播、热搜词、收藏以及商品详情页面的展示；添加购物车、个人订单以及集成第三方支付接口（如支付宝）等功能；

使用方法：
-------
1.安装Python3.6环境
-------
2.下载代码到本地并解压
-------
3.cmd到根目录下安装相关依赖包
-------
```
pip install -r requirements.txt
```
4.安装mysql数据库，进入mysite/settings.py配置数据库连接
-------

```DATABASES = {
‘default’: {
    # 'ENGINE': 'django.db.backends.sqlite3',
    # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'ENGINE':'django.db.backends.mysql',     # 数据库类型，mysql
    'NAME':'mxshop',            #  database名
    'USER':'root',               # 登录用户
    'PASSWORD':'123456',        #  登录用户名
    'HOST':'127.0.0.1',        # 数据库地址
    'PORT':'3306'              # 数据库端口
}
}
```
5.cmd到根目录下，生成数据库迁移记录
-------
```
python manage.py makemigrations
```
6.完成数据库迁移
-------
```
python manage.py migrate 
```
7.创建超级用户，用于后台管理
-------
```
python manage.py createsuperuser
```
8.运行启动django服务
-------
```
python manage.py runserver 127.0.0.1:8000
```
8.cmd进入online-store目录下，运行前端Vue项目
-------
```
cnpm run dev
```
9.访问127.0.0.1:8080进入生鲜电商平台主页
-------
主页：
![](https://github.com/PyGuojun/MxShop/blob/master/image/my_logo.png)

商品分类：
![](https://github.com/PyGuojun/MxShop/blob/master/image/shop_category.png)

加入购物车：
![](https://github.com/PyGuojun/MxShop/blob/master/image/shop_car.png)

购物车订单：
![](https://github.com/PyGuojun/MxShop/blob/master/image/order.png)

订单支付：
![](https://github.com/PyGuojun/MxShop/blob/master/image/pay.png)

个人中心：
![](https://github.com/PyGuojun/MxShop/blob/master/image/personal.png)
