
# pyinstaller
https://github.com/pyinstaller/pyinstaller
下载zip文件再解压，将解压后的文件直接放在anaconda\Lib\site-package文件夹中全部替换pyinstaller，然后打开命令行，进入到解压后的PyInstaller文件的目录下，输入：

python setup.py install

# zipapp模块进行打包
```
"""
app文件夹
..app.py
..hello文件夹
  ..__init__.py
  ..hello.py
"""


# app.py
from hello.hello import say
def main():
    print("wo shi app")
    print(say())
    
# hello.py
def say():
    return "say hello !"
```

```
python -m zipapp app -m "app:main"
 
 app是app文件夹
 app:main 是如口，app.py中的main函数

生成了 app.pyz
直接python app.pyz 就可以执行了。


第三方库
# 这条命令是将安装包安装到app文件夹里，我们写的使用，可以不放到这
# 只要符合模块导入规则，找到到就可以
python -m pip install -r requirements.txt --target app

# 然后打包就ok了
python -m zipapp app -m "app:main"
```


# setuptools
[参考](https://blog.csdn.net/chenfeidi1/article/details/80873979)

一个是打包成egg文件：python setup.py bdist_egg 。
执行完成后，会在同目录下多了两个文件夹：demo.egg-info和dist，egg文件就在dist中，这个文件可以上传到pypi.python.com上，供大家下载。
或者上传到某网盘，通过pip install --no--index find-links=[url]来下载。
另外一种是打包成压缩文件形式：python setup.py sdist 。执行结果同上，不过文件格式不同。

打包完成之后，当然要安装了，上一篇介绍了virtualenv，创建一个虚拟环境以供测试。
然后执行python setup.py install 就会在你的虚拟环境的bin下创建一个demo的可执行文件，你在虚拟环境中运行：demo，输出结果。
```
python setup.py --help
#查看setup文件的配置信息可以包含哪些

python setup.py --help-commands
# 查看程序打包和分发可以使用的命令有哪些
```
- 创建egg包：“python setup.py bdist_egg”
- 创建wheel包：“python setup.py bdist_wheel” 
    参数：--universal 通用 wheel 包

官方推荐wheel包格式 https://packaging.python.org/discussions/wheel-vs-egg/

主要分为两类：sdist 和 bdist

## Source distribution
使用 sdist 可以打包成 source distribution，支持的压缩格式有：

Format	| Description |	Notes
---|---|---
zip|	zip file (.zip)|	Windows 默认
gztar|	gzip’ed tar file (.tar.gz)	|Unix 默认
bztar|	bzip2’ed tar file (.tar.bz2)	
xztar|	xz’ed tar file (.tar.xz)	
ztar|	compressed tar file (.tar.Z)	
tar|	tar file (.tar)	

`python setup.py sdist --formats=gztar,zip`如果不指定则如上表根据具体平台默认格式打包。

## Built distribution
和源码包相比，由于预先构建好，所以安装更快：

Format |	Description|	Notes
---|---|---
gztar|	gzipped tar file (.tar.gz)	|Unix 默认
bztar|	bzipped tar file (.tar.bz2)	
xztar|	xzipped tar file (.tar.xz)	
ztar|	compressed tar file (.tar.Z)	
tar	|tar file (.tar)	
zip|	zip file (.zip)|	Windows 默认
rpm	|RPM	
pkgtool	|Solaris pkgtool	
sdux|	HP-UX swinstall	
wininst	|self-extracting ZIP file for Windows	
msi	|Microsoft Installer.	

`python setup.py bdist --formats=rpm`

同时为了简化操作，setuptools 提供了如下命令：

Command	|Formats|	Notes
---|---|---
bdist_dumb	|tar, gztar, bztar, xztar, ztar, zip	|Windows 默认 zip, Unix 默认 gztar
bdist_rpm	|rpm, srpm	
bdist_wininst|	wininst	
bdist_msi|	msi	
...|

> 如果使用 bdist_wininst，打出来的是 exe 安装文件，可以点击安装。
>
> 使用 develop 开发模式安装的话，实际代码不会拷贝到 site-packages 下，而是除一个指向当前应用的链接（*.egg-link）。这样当前位置的源码改动就会马上反映到 site-packages。使用如下：
>
> $ pip install -e .  # 或者 python setup.py develop
> pip install --no-deps .(注意：结尾有个.，代表当前路径) 代替 python setup.py install

## setuptools

Setuptools 是 Python Distutils 的加强版，使开发者构建和发布 Python 包更加容易，特别是当包依赖于其他包时。用 setuptools 构建和发布的包与用 Distutils 发布的包是类似的。包的使用者无需安装 setuptools 就可以使用该包。如果用户是从源码包开始构建，并且没有安装过 setuptools 的话，则只要在你的 setup 脚本中包含一个 bootstrap 模块（ez_setup），用户构建时就会自动下载并安装 setuptools 了。

```s
$ pip install --upgrade setuptools
```

### 基础用例

```py
from setuptools import setup, find_packages
setup(
    name = "HelloWorld",
    version = "0.1",
    packages = find_packages(),
)
```

上面就是一个最简单的 setup 脚本，使用该脚本，就可以产生 eggs，上传 PyPI，自动包含 setup.py 所在目录中的所有包等。当然，上面的脚本过于简单，下面是一个稍微复杂的例子：

```py
from setuptools import setup, find_packages
setup(
    name = "HelloWorld",
    version = "0.1",
    packages = find_packages(),
    scripts = ['say_hello.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
    # metadata for upload to PyPI
    author = "Me",
    author_email = "me@example.com",
    description = "This is an Example Package",
    license = "PSF",
    keywords = "hello world example examples",
    url = "http://example.com/HelloWorld/",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)
```

# 工具函数

## find_packages

对于简单的工程，使用 setup 函数的 packages 参数一一列出安装的包到就足够了。但是对于大型工程来说，这却有点麻烦，因此就有了 setuptools.find_package() 函数。find_packages 的参数有：一个源码目录，一个 include 包名列表，一个 exclude 包名列表。如果这些参数被忽略，则源码目录默认是 setup.py 脚本所在目录。该函数返回一个列表，可以赋值给 packages 参数。

有些工程可能会使用 src 或者 lib 目录作为源码树的子目录，因此这些工程中，需要使用”src”或者”lib”作为 find_packages()的第一个参数，当然，这种情况下还需要设置 package_dir = {'':'lib'}，否则的话会报错，比如 setup 脚本如下：

```py
from setuptools import setup, find_packages
setup(
    name = "HelloWorld",
    version = "0.1",
    package_dir = {'':'lib'},
    packages = find_packages('lib'),
)
```

源码树如下：

```s
lib/
    foo.py
    heheinit.py
    bar/
        __init__.py
        bar.py
```

最终生成的文件如下：

```s
/usr/local/lib/python2.7/dist-packages/HelloWorld-0.1-py2.7.egg-info/dependency_links.txt
/usr/local/lib/python2.7/dist-packages/HelloWorld-0.1-py2.7.egg-info/PKG-INFO
/usr/local/lib/python2.7/dist-packages/HelloWorld-0.1-py2.7.egg-info/SOURCES.txt
/usr/local/lib/python2.7/dist-packages/HelloWorld-0.1-py2.7.egg-info/top_level.txt
/usr/local/lib/python2.7/dist-packages/bar/bar.py
/usr/local/lib/python2.7/dist-packages/bar/bar.pyc
/usr/local/lib/python2.7/dist-packages/bar/__init__.py
/usr/local/lib/python2.7/dist-packages/bar/__init__.pyc
```

如果没有 `package_dir = {'':'lib'}` 的话，则会报错：

```s
error: package directory 'bar' does not exist
```

这是因为执行函数 find_packages('lib')，返回的结果是['bar']，没有 package_dir = {'':'lib'}的话，则在 setup.py 所在目录寻找包 bar，自然是找不到的了。

```s
>>> import setuptools
>>> setuptools.find_packages('lib')
['bar']
```

find_packages()函数遍历目标目录，根据 include 参数进行过滤，寻找 Python 包。对于 Python 3.2 以及之前的版本，只有包含 `__init__.py` 文件的目录才会被当做包。最后，对得到的结果进行过滤，去掉匹配 exclude 参数的包。include 和 exclude 参数是包名的列表，包名中的’.’表示父子关系。比如，如果源码树如下：

```s
lib/
    foo.py
    __init__.py
    bar/
        __init__.py
        bar.py
```

则 find_packages(exclude=["lib"])（或 packages = find_packages(include=["lib"])），只是排除（或包含）lib 包，但是却不会排除（或包含 lib.bar）包。

## entry points

entry points 是发布模块“宣传”Python 对象（比如函数、类）的一种方法，这些 Python 对象可以被其他发布模块使用。一些可扩展的应用和框架可以通过特定的名字找到 entry points，也可以通过发布模块的名字来找到，找到之后即可加载使用这些对象了。entry points 要属于某个 entry points 组，组其实就是一个命名空间。在同一个 entry point 组内不能有相同的 entry point。

entry points 通过 setup 函数的 entry_points 参数来表示，这样安装发布包之后，发布包的元数据中就会包含 entry points 的信息。entry points 可以实现动态发现和执行插件，自动生成可执行脚本、生成可执行的 egg 文件等功能。setup 函数的 entry_points 参数，可以是 INI 形式的字符串，也可以是一个字典，字典的 key 是 entry point group 的名字，value 是定义 entry point 的字符串或者列表。

一个 entry point 就是 `name = value` 形式的字符串，其中的 value 就是某个模块中对象的名字。另外，在”name = value”中还可以包含一个列表，表示该 entry point 需要用到的”extras”，当调用应用或者框架动态加载一个 entry point 的时候，”extras”表示的依赖包就会传递给 pkg_resources.require()函数，因此如果依赖包没有安装的话就会打印出相应的错误信息。

比如 entry_points 可以这样写：

```py
setup(
    ...
    entry_points = """
        [blogtool.parsers]
        .rst = some.nested.module:SomeClass.some_classmethod[reST]
    """,
    extras_require = dict(reST = "Docutils>=0.3.5")
    ...
)
setup(
    ...
    entry_points = {'blogtool.parsers': '.rst = some_module:SomeClass[reST]'}
    extras_require = dict(reST = "Docutils>=0.3.5")
    ...
)
setup(
    ...
    entry_points = {'blogtool.parsers': ['.rst = some_module:a_func[reST]']}
    extras_require = dict(reST = "Docutils>=0.3.5")
    ...
)
```