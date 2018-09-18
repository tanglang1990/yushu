## pipenv

Pipenv，它的项目简介为 Python Development Workflow for Humans，是 Python 著名的 requests 库作者 kennethreitz 写的一个包管理工具，它可以为我们的项目自动创建和管理虚拟环境并非常方便地管理 Python 包，现在它也已经是 Python 官方推荐的包管理工具。

Pipenv 我们可以简单理解为 pip 和 virtualenv 的集合体，它可以为我们的项目自动创建和管理一个虚拟环境。virtualenv 在使用时我们需要手动创建一个虚拟环境然后激活，Pipenv 会自动创建。另外我们之前可能使用 requirements.txt 文件来标识项目所需要的依赖，但是这样会带来一些问题，如有的 requirements.txt 中只是将库名列出来了，没有严格指定版本号，这样就可能会导致不同时间安装的库版本是不同的，如 requirements.txt 文件中对 Django 的依赖只写了一个 django，可能在 2016 年的时候运行安装会安装 Django 的 1.x 版本，到了 2017 年就会安装 Django 的 2.x 版本，所以可能导致一些麻烦。为了解决这个问题，Pipenv 直接弃用了 requirements.txt，会同时它会使用一个叫做 Pipfile 和 Pipfile.lock 的文件来管理项目所需的依赖包，而不再是简单地使用 requirements.txt 文件来记录项目所需要的依赖


### 总的来说，Pipenv 可以解决如下问题：
1. 我们不需要再手动创建虚拟环境，Pipenv 会自动为我们创建，它会在某个特定的位置创建一个 virtualenv 环境，然后调用 pipenv shell 命令切换到虚拟环境。
1. 使用 requirements.txt 可能会导致一些问题，所以 Pipenv 使用 Pipfile 和 Pipfile.lock 来替代之，而且 Pipfile 如果不存在的话会自动创建，而且在安装、升级、移除依赖包的时候会自动更新 Pipfile 和 Pipfile.lock 文件。
1. 广泛使用 Hash 校验，保证安全性。
1. 可以更清晰地查看 Python 包及其关系，调用 pipenv graph 即可呈现，结果简单明了。
1. 可通过自动加载 .env 读取环境变量，简化开发流程。

### 参考文档
1. github: https://github.com/pypa/pipenv
1. pypi: https://pypi.org/project/pipenv/
1. 用法: https://pipenv.readthedocs.io/en/latest/#pipenv-usage

### 安装
   >pip install pipenv

### 常用命令
* pipenv --help

查看帮助文档，非常重要（其实靠此一招，即可走遍天下）
在忘记命令的时候也可以派上用场
    
* `pipenv shell`

进入虚拟环境shell，之前在当前目录下没有虚拟环境，会先创建虚拟环境

* `exit`

进入虚拟环境shell之后退出环境

* `pipenv install`

创建虚拟环境, 如果已经有Pipefile和Pipefile.lock会依据这两个文件创建虚拟环境。

* `pipenv --venv`

查看虚拟环境路径

* `pipenv --py`

获取虚拟环境 Python 解释器路径

* `pipenv --three`  或者 `pipenv --python 3.6` 

创建一个 Python3 的虚拟环境，–three 代表创建一个 Python3 版本的虚拟环境，–python 则可以指定特定的 Python 版本，当然 –two 则创建一个 Python2 版本的虚拟环境，但前提你的系统必须装有该版本的 Python 才可以。

* `pipenv install django`

安装包

项目路径下会自动生成了一个 Pipfile.lock 

可以看到里面标识了 Python 环境基本信息，以及依赖包的版本及 hashes 值。

另外我们还可以注意到 Pipfile 文件内容也有更新，[packages] 部分多了一句 django = “*”，标识了本项目依赖于 Django，这个其实类似于 requirements.txt 文件。

那么到这里有小伙伴可能就会问了， Pipfile 和 Pipfile.lock 有什么用呢？

Pipfile 其实一个 TOML 格式的文件，标识了该项目依赖包的基本信息，还区分了生产环境和开发环境的包标识，作用上类似 requirements.txt 文件，但是功能更为强大。

Pipfile.lock 详细标识了该项目的安装的包的精确版本信息、最新可用版本信息和当前库文件的 hash 值，顾明思义，它起了版本锁的作用，可以注意到当前 Pipfile.lock 文件中的 Django 版本标识为 ==2.0.2，意思是当前我们开发时使用的就是 2.0.2 版本，它可以起到版本锁定的功能。

举个例子，刚才我们安装了 Django 2.1.1 的版本，即目前的最新版本。但可能 Django 以后还会有更新，比如某一天 Django 更新到了 2.1 版本，这时如果我们想要重新部署本项目到另一台机器上，假如此时不存在 Pipfile.lock 文件，只存在 Pipfile文件，由于 Pipfile 文件中标识的 Django 依赖为 django = “*”，即没有版本限制，它会默认安装最新版本的 Django，但由于 Pipfile.lock 文件的存在，它会根据 Pipfile.lock 来安装，还是会安装 Django 2.1.1，这样就会避免一些库版本更新导致不兼容的问题。

请记住：任何情况下都不要手动修改 Pipfile.lock 文件！

* `pipenv graph`

查看包与包之间的依赖关系

* `pipenv uninstall requests`

卸载 Python 包

卸载完成之后，Pipfile 和 Pipfile.lock 文件同样会更新。

*  `pipenv uninstall --all`

卸载全部 Python 包

* `pipenv lock`

可能 Pipfile.lock 文件不存在或被删除了，这时候我们可以使用如下命令生成

### 结语

作为 pip 和 virtualenv 的结合体，我们可以利用它更方便地创建和管理 Python 虚拟环境，还可以用更加科学的方式管理 Python 包

是时候抛弃 virtualenv 和 pip 了!