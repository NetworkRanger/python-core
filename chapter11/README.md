# Web框架：Django

## 项目和应用

### 在Django中创建项目

#### Django 项目文件

文件名|描述/用途
-----|--------  
 __init__.py|告诉 Python 这是一个软件包
urls.py|全局 URL 配置(“URLconf”)
settings.py|项目相关的配置
manage.py|应用的命令行接口

### "Hello World"应用（一个博客）

#### Django 应用文件 

文件名|描述/目的
-----|------
__init__.py|告诉 Python 这是一个包
urls.py|应用的 URL 配置文件(“URLconf”)，这个文件并不像项目的 URLconf 那样自动创建(所 以上面的截图中没有)
models.py|数据模型
views.py|视图函数(即 MVC 中的控制器) 
tests.py|单元测试

## 中级Django应用： TweetApprover

### URL结构

#### 项目处理的 URL 以及对应的行为

URL|行为
----|----
/post|提交新推文
/post/edit/X|编辑 ID 为 X 的推文
/post/thankyou|在用户提交推文后显示致谢页面
/|与/post 相同 
/approve|列出所有待审核和已发布的推文
/approve/review/X|用于审核推文 X
/admin|转到项目的 admin 页面
/login|用户登录
/logout|用户注销

## 资源

#### 其他 Web 框架和资源

包| 资源
---|------
Django|http://djangoproject.com
Pyramid & Pylons|http://pylonsproject.org
TurboGears|http://turbogears.org
Pinax|http://pinaxproject.com
Python Web Frameworks|http://wiki.python.org/moin/WebFrameworks
Django-nonrel|http://www.allbuttonspressed.com
virtualenv|http://pypi.python.org/pypi/virtualenv
Twitter Developers|http://dev.twitter.com
OAuth|http://oauth.net