# Python简介与安装

### Python版本说明

Python2与Python3语法上有差异，不兼容。（Python2写的代码不能在Python3平台上面运行，Python3写的代码也不能在Python2环境下运行）

**如何选择版本：**
考虑自己准备使用的模块是否支持2.x和3.x

**建议：**
建议先学python2，熟练之后再学习一下python3

### 一个建议
如果是从事运维和云计算方面的开发，建议学习python2。因为目前大部分云计算的产品都提供了python2的支持，但是不一定提供python3的支持。

### 安装Python2.7.x (CentOS 6.x)
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

### 安装python包管理工具pip

```
yum install -y wget
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

编辑\~/.pip/pip.conf(没有则创建)

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
### Hello World
```
print 'hello world'
```

### python程序
python源程序文件通常以.py为扩展名，如下，新建一个名为test.py

```python
#!/usr/bin/python               //指明脚本文件的解释程序。
import platform
print platform.uname()
```

### centos7源码安装python3

	yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel gcc

### git使用
1. github注册账号，确认账号
2. 在github网站上面，建一个项目

git clone [https://github.com/cudatec01/zanqi\_python\_training.git][1]

git status 查看项目文件的变化
git add \<filename\> 将文件添加到暂存区
git commit -m ‘description’
git push 同步本地仓库到github上面的远程仓库

[1]:	https://github.com/cudatec01/zanqi_python_training.git