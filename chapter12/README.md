# 云计算: Google App Engine

## 沙盒和App Engine SDK

### 服务和API

#### Google App Engine 的服务与 API(有些为实验性的)
 
服务/API|说明
--------|----
App Identity|用于应用或其他 API 请求信息时用来进行身份验证 
Appstats|基于事件的框架，帮助衡量应用的性能
Backends|如果标准的请求/响应或任务队列的截止期限无法满足需求，可以使用 Backends API 让 App Engine 的 代码继续执行
Blobstore|Blobstore 可以让应用处理大于 Datastore 限制的数据对象(如媒体文件) 
Capabilities|让应用能够检测 App Engine 的 Datastore 或 Memcache 是否可用 
Channel|直接向浏览器推送数据，即 Reverse Ajax、browser push、Comet 
Cloud SQL|使用关系数据库(而不是默认的可扩展的分布式 Datastore)
Cloud Storage|使用 Files API(参见这张表后面的描述)，直接向 Google Cloud Storage 读写文件 
Cronversion|使用这个 API 在 HTML、PDF 格式、文本和图像格式之间转换
Cron|使用 Cron 能够在特定的日期、时间或时间间隔运行计划任务 
Datastore|一个分布式、可扩展、非关系持久性数据存储
Denial-of-Service|使用这个 API 来设置过滤器，屏蔽发布拒绝服务(DoS)攻击应用程序的 IP 地址 
Download|在发生灾难时，开发人员可以下载上传到 Google 的代码。
Files|使用常见的 Python 文件接口创建分布式的(blobstore 或 Cloud Storage)文件
(Full-text)Search|在 Datastore 中搜索文本、时间戳等 
Images|处理图像数据;例如，创建缩略图、裁切、调整大小和旋转图像
Logs|允许用户访问应用程序和日志请求，甚至对于长时间运行的请求，在运行时进行清理 
Mail|这个 API 让应用程序能够发送和/或接收电子邮件 
MapReduce|在非常大的数据集上执行分布式计算。包括 map、shuffle、 reduce 阶段的 API 
Memcache|高扩展的实时匹配基础设施:注册查询来匹配对象流 在应用程序和持久性存储之间的标准分布式内存数据缓存(类似 Memcached) 
Namespaces(Multienancy)|使用命名空间，通过划分 Google App Engine 数据，创建多租户的应用程序
NDB(新数据库)|新的实验性的 Python-App 引擎高级 Datastore 接口
OAuth|为第三方提供一种代表用户访问数据的安全方法，无需授权(登录/密码等)
OpenID|用户可以使用 Google 账户和 OpenID 账户登录联合身份验证服务
Pipeline|管理多个长时间运行的任务/工作流，并整理运行的结果
Prospective Search|有些与允许用户搜索现有数据的全文检索 API 相比，Prospective Search 允许用户查询尚未创建的数 据:设置查询，当存储匹配的数据时，调用 API(想想数据库触发器加上任务队列)
Socket|允许用户通过出站套接字连接来创建并通信 
Task Queue|无需用户交互就可以执行后台任务(可以并发执行)
URLfetch|通过 HTTP 请求/响应与其他应用程序在线通信
Users|App Engine 的身份验证服务，管理用户的登录过程 
WarmUp|流量到来之前在实例中加载应用程序以缩短请求服务时间 
XMPP|让应用能够通过 Jabber / XMPP 协议来聊天(发送和/或接收即时消息)

## 选择一个App Engine框架

#### 用于 Google App Engine 的框架

框架|描述
----|----
webapp、webapp2|App Engine SDK 自带的轻量级 Web 框架
bottle|Python 中的一个轻量级 WSGI 微型 Web 框架;附带 App Engine 适配器(gae)
Django|Django 是一款流行的 Python 全栈 Web 框架(在 GAE 中并非所有功能都可用)
Django-nonrel|用于在非关系数据存储(如 GAE)上运行 Django 应用程序
Flask|另一个微型框架(像上面的“bottle”)，基 于 Werkzeug & Jinja2(像下面的 Kay)，易于定制，没有 本地数据抽象层，直接使用 App Engine 的 Datastore
GAE Framework Google App|基于 Django，但是简化过。使用这个框架可以重用已有的应用架构，如 users、blog、admin 等。可 以认为是用于 App Engine 的 Django + Pinax 简化版
Google App Engine Oil(GAEO)|如果 Web 应用太简单，而 Django 太复杂，可以使用这个 MVT 框架，与 Django 类似，也是受到了 Ruby 的 Rails 和 Zend 框架的启发
Kay|与 Django 类似，但使用 Werkzeug 作为低层框架、使用 Jinja2 作为模板引擎、使用 babel 来翻 译语言
MVCEngine|受到 Rails 和 ASP.NET 启发的框架
Pyramid|另一种流行全栈 Web 框架，基于 Pylons 和 repoze.bfg
tipfy|比 webapp 更强大的轻量级框架，只为 App Engine 而建。这也导致 webapp2 的创建，意味着最初的 创造者不再维护这个框架
web2py|另一款 Python 全栈 Web 框架，有较高的抽象级别，这意味着它比其他的框架更容易使用，但隐藏 了更多的细节(有好有坏)

#### 与Google App Engine共同开发的框架

项目|URL
----|---
Google App Engine|http://code.google.com/appengine 
Bigtable|http://labs.google.com/papers/bigtable.html
Megastore|http://research.google.com/pubs/pub36971.html
webapp|http://code.google.com/appengine/docs/python/gettingstarted/usi ngwebapp.html
webapp|http://code.google.com/appengine/docs/python/tools/
webapp2|http://code.google.com/appengine/docs/python/gettingstartedpyth on27/usingwebapp.html
webapp2|http://code.google.com/appengine/docs/python/tools/ webapp
webapp2|http://webapp-improved.appspot.com/
Django|http://djangoproject.com
Django-nonrel|http://www.allbuttonspressed.com/projects/django-nonrel
djangoappengine|http://www.allbuttonspressed.com/projects/ djangoappengine
Bottle|http://bottlepy.org
Flask|http://flask.pocoo.org/
tipfy|http://tipfy.org
web2py|http://web2py.com
AppScale|http://appscale.cs.ucsb.edu
TyphoonAE|http://code.google.com/p/typhoonae
