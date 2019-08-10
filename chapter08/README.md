# 扩展Python

## 编写Python扩展

### 根据样板编写封装代码

#### 在 Python 和 C/C++之间转换数据

函数|说明
----|----
从 Python 到 C|
int PyArg_ParseTuple()|将位于元组中的一系列参数从 Python 转化为 C 
int PyArg_ParseTupleAndKeywords()|与上一个类似，但还会解析关键字参数
从 C 到 Python|
PyObject*Py_BuildValue()|将 C 数据值转化为 Python 返回对象，要么是单个对象，要么是一个含有多个对象的元组
               
#### Python1和 C/C++之间的“转换编码”
 
格式编码|Python 数据类型|C/C++数据类型
-------|--------------|-----------
s、s#|str/unicode, len()|Char*(, int)
z、z#|str/unicode/None,len()|char*/NULL(, int)
u、u#|unicode, len()|(Py_UNICODE*, int) int
i|int|int
b|int|char
h|int|short
l|int|long
k|int 或 long|unsinged long
I|int 或 long|unsigned int
B|int|unsigned char
H|int|unsigned short
L|long|long long
K|long|unsing long long
c|str|char
d|float|double
f|float|float
D|complex|Py_COmplex *
O|（任意类型)|PyObject *
S|str|PyStringObject
N|（任意类型)|PyObject *
O&|（任意类型)|（任意类型)

### 引用计数

#### 用于执行 Python 对象引用计数的宏

函数|说明
----|---
Py_INCREF(obj)|递增对象 obj 的引用计数
Py_DECREF(obj)|递减对象 obj 的引用计数
