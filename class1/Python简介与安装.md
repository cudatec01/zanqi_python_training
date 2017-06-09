# Python简介与安装

Python诞生于1989年，作者希望能够创造出一种C和shell之间，功能全面，易学易用的可扩展语言。

## Python版本说明

Python2与Python3语法上有差异，不兼容。（Python2写的代码不能在Python3平台上面运行，Python3写的代码也不能在Python2环境下运行）

Python2.7的支持到2020年结束。（www.python.org)

**如何选择版本：**

1. 考虑自己的项目准备使用的第三方模块是否支持2.x和3.x
2. 如果2.x和3.x都支持，建议选择3.x

**个人建议：**

两个都学

1. 云计算相关开发

如果是从事运维和云计算方面的开发，建议学习python2。因为目前大部分云计算的产品都提供了python2的支持，但是不一定提供python3的支持。

2. autodesk相关开发

学习python2.7，只提供了python2.x的支持。

**Why Python3 exists**

1. Text and binary data in Python 2 are a mess

## 安装Python2.7.x

### CentOS 6.x 编译安装

1.安装开发工具包

```
sudo yum groupinstall "Development Tools" -y
```

2.安装编译python所依赖的库

```
sudo yum install -y readline readline-devel zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
```

3.去python官网下载源码包(https://www.python.org)

```
tar -zxvf Python-2.7.11.tgz
cd Python-2.7.11
./configure --prefix=/usr/local
sudo make && sudo make install

sudo rm -f /usr/bin/python
sudo ln -sv /usr/local/bin/python /usr/bin/python
```

**注意**：修改yum程序：yum程序只能使用python2.6，不支持2.7，因此需要修改yum程序的代码：
编辑sudo vi /usr/bin/yum程序，将文件开头的#!/usr/bin/python改为#!/usr/bin/python2.6

4.验证
控制台输入python -V，正确返回Python版本，即表示安装成功。

```
[lvjin@localhost ~]$ python -V
Python 2.7.11
```

### windows10

下载exe文件双击安装。

### 安装python包管理工具pip

```
yum install -y wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

编辑~/.pip/pip.conf(没有则创建)

```
[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple
```

### 下载安装ipython

ipython是一个python的交互式shell，比默认的python shell好用的多，支持变量自动补全，自动缩进，支持bash shell命令，内置了许多很有用的功能和函数。

```
sudo pip install ipython
```

安装完之后，在控制台输入ipython，进入ipython的交互界面。

## Hello World

```
print 'hello world'
```

## python程序

python源程序文件通常以.py为扩展名，如下，新建一个名为test.py

```python
#!/usr/bin/python				//指明脚本文件的解释程序。
import platform
print platform.uname()
```
