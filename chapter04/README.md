# 多线程编程

## thread模块

#### thread 模块和锁对象

函数/方法|描述
--------|---
thread 模块的函数|
start_new_thread (function, args, kwargs=None)|派生一个新的线程，使用给定的 args 和可选的 kwargs 来执行 function 
allocate_lock()|分配 LockType 锁对象
exit()|给线程退出指令
LockType 锁对象的方法|
acquire (wait=None)|尝试获取锁对象
locked ()|如果获取了锁对象则返回 True，否则，返回 False 
release ()|释放锁

## threading模块

#### threading 模块的对象

对象|描述
----|----
Thread|表示一个执行线程的对象  
Lock|锁原语对象(和 thread 模块中的锁一样)
RLock|可重入锁对象，使单一线程可以(再次)获得已持有的锁(递归锁)
Condition|条件变量对象，使得一个线程等待另一个线程满足特定的“条件”，比如改变状态或 某个数据值
Event|条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有 线程将被激活
Semaphore|为线程间共享的有限资源提供了一个“计数器”，如果没有可用资源时会被阻塞
BoundedSemaphore|与 Semaphore 相似，不过它不允许超过初始值
Timer|与 Thread 相似，不过它要在运行前等待一段时间
Barrier|创建一个“障碍”，必须达到指定数量的线程后才可以继续

### Thread类

#### Thread对象的属性和方法

属性|描述
----|---
Thread对象的数据属性|
name|线程各
ident|线程的标识符
daemon|布尔标志，表示这个线程是否是守护线程
Thread对象方法|
_init_(group=None, tatget=None, name=None, args=(), kwargs ={}, verbose=None, daemon=None)|实例化一个线程对象，需要有一个可调用的 target，以及其参数 args 或 kwargs。还可以传递 name 或 group 参数，不过后者还未实现。此 外，verbose 标志也是可接受的。而 daemon 的值将会设定 thread.daemon 属性/标志
start()|开始执行该线程 
run()|定义线程功能的方法(通常在子类中被应用开发者重写)
join (timeout=None)|直至启动的线程终止之前一直挂起;除非给出了 timeout(秒)，否则 会一直阻塞
getName()|返回线程名
setName (name)|设定线程名
isAlivel /is_alive ()|布尔标志，表示这个线程是否还存活
isDaemon()|如果是守护线程，则返回 True;否则，返回 False
setDaemon(daemonic)|把线程的守护标志设定为布尔值 daemonic(必须在线程 start()之前 调用)

### threading 模块的其他函数

#### threading 模块的函数

函数|描述
activeCount/active_count()|当前活动的 Thread 对象个数
currentThread()/current_thread|返回当前的 Thread 对象
enumerate()|返回当前活动的 Thread 对象列表
settrace(func)|为所有线程设置一个 trace 函数
setprofile(func)|为所有线程设置一个 profile 函数
stack_size(size=0)|返回新创建线程的栈大小;或为后续创建的线程设定栈的大小 为 size

## 生产者-消费者问题和 Queue/queue 模块

#### Queue/queue 模块常用属性

属性|描述
----|----
Queue/queue模块的属性|
Queue(maxsize=0)|创建一个先入先出队列。如果给定最大值，则在队列没有空间时阻塞;否则(没 有指定最大值)，为无限队列
LifeQueue(maxsize=0)|创建一个后入先出队列。如果给定最大值，则在队列没有空间时阻塞;否则(没 有指定最大值)，为无限队列
PriorityQueue(maxsize=0)|创建一个优先级队列。如果给定最大值，则在队列没有空间时阻塞，否则(没有指定最大值),为无限队列
Queue/queue异常|
Empty|当对空队列调用 get*()方法时抛出异常
Full|当对已满的队列调用 put*()方法时抛出异常
Queue/queue对象方法|
qsize()|返回队列大小(由于返回时队列大小可能被其他线程修改，所以该值为近似值)
empty()|如果队列为空，则返回 True;否则，返回 False
full()|如果队列已满，则返回 True;否则，返回 False
put(item,block=True,timeout=None)|将 item 放入队列。如果 block 为 True(默认)且 timeout 为 None，则在有可用 空间之前阻塞;如果timeout为正值，则最多阻塞timeout秒;如果 block为False， 则抛出 Empty 异常
put_nowait(item)|和 put(item, False)相同
get(block=True,timeout=None)|从队列中取得元素。如果给定了 block(非0)，则一直阻塞到有可用的元素为止
get_nowait()|和 get(False)相同
task_donw()|用于表示队列中的某个元素已执行完成，该方法会被下面的 join()使用 
join()|在队列中所有元素执行完毕并调用上面的 task_done()信号之前，保持阻塞

## 相关模块

#### 与线程相关的标准库模块

模块|描述
----|---
thread|基本的、低级别的线程模块 
threading|高级别的线程和同步对象
multiprocessing|使用“threading”接口派生/使用子进程
subprocess|完全跳过线程，使用进程来执行
Queue|供多线程使用的同步先入先出队列
mutex|互斥对象
concurrent.futures|异步执行的高级别库
SocketServer|创建/管理线程控制的 TCP/UDP 服务器