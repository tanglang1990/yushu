# Jinja2模板语言（引擎）
Jinja2 是一个现代的，设计者友好的，仿照 Django 模板的 Python 模板语言编写。 

## Jinja2 官方文档

* [http://jinja.pocoo.org/docs/2.10/](http://jinja.pocoo.org/docs/2.10/) （英文）
* [http://docs.jinkan.org/docs/jinja2/](http://docs.jinkan.org/docs/jinja2/) （中文）

## 学习方法
* 关键的需要记住
* 但不是所有的都要求记住，需要用的时候知道去官方文档查看即可

## 安装
```
$ pip install Jinja2
```

## Jinja2的模板渲染

### 为什么使用模板

* 动态生成html
* 解耦，业务逻辑和页面展示分离

### 如何使用模板渲染
1. 获取模板内容
2. 进行渲染
    ```
    >>> from jinja2 import Template
    >>> template = Template('Hello {{ name }}!')
    >>> template.render(name='John Doe')
    u'Hello John Doe!'
    >>> template.render({'name': 'ten'})
    u'ten'
    ```

## API
1.加载文档
* Jinja2 使用一个名为 Environment 的中心对象。这个类的实例用于存储配 置、全局对象，并用于从文件系统或其它位置加载模板。
* 即使你通过:class:Template 类的构造函数用字符串创建模板，也会为你自动创建一个环境
```python
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('yourapplication', 'templates'))
"""
这会创建一个默认设定下的模板环境和一个在 yourapplication python 包中的 templates 文件夹中寻找模板的加载器。
多个加载器是可用的，如果你需要从 数据库或其它资源加载模板，你也可以自己写一个。
你只需要调用 get_template() 方法从这个环境中加载模板，并会返回已加载的 Template:
"""
template = env.get_template('mytemplate.html')
print(template.render(the='variables', go='here'))
```

## 模板的基本用法

[参考文档 http://docs.jinkan.org/docs/jinja2/templates.html](http://docs.jinkan.org/docs/jinja2/templates.html)

1. 渲染变量

   `{{ 变量名 }}`

   * 把变量传递到模板
   * 花括号 不是 变量的一部分，而是打印语句的一部分是重要的, 可以看作print\(变量名\)
   * 你可以使用点（ . ）来访问变量的属性，作为替代，也可以使用所谓的“下标”语 法（ [] ）。下面的几行效果是一样的:
        ```
       {{ foo.bar }}
       {{ foo['bar'] }}
        ```

2. 过滤器  
    `{{ 变量名|过滤器 }}`

   * 内置过滤器 

        [清单 http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters)

   * 自定义过滤器  
     1. 定义函数，注意过滤器至少接收一个参数，就是被过滤的变量本身  
     2. 注册自定义过滤器(不鼓励使用自定义过滤器)
        ```python
        from flask import Flask
        from flask_script import Manager
        from flask import render_template
        
        app = Flask(__name__)
        manager = Manager(app)
        
        def mylen(arg):#实现一个可以求长度的函数
            return len(arg)
        
        # 该函数实现给定一个区间返回区间的内容
        def interval(test_str, start, end):#过滤器中传递多个参数，第一个参数为被过滤的内容，第二第三个参数需要自己传入
            return test_str[int(start):int(end)]
        
        env = app.jinja_env
        env.filters['mylen'] = mylen#注册自定义过滤器
        env.filters['interval'] = interval#注册自定义过滤器
        ```
     > 标签和过滤器是为了复杂模板的设计人员（可能不会Python）能够通过借此实现复杂效果，Python开发人员应该学会这种用法和思想，但是在实践中不鼓励使用自定义标签


3. 测试

   `{% 标签 %}`

   * 可以看作一个函数在执行
    ```
    {% if loop.index is divisibleby 3 %}
    {% if loop.index is divisibleby(3) %}
    ```
   * 内置标签 [清单 http://docs.jinkan.org/docs/jinja2/templates.html#tests](http://docs.jinkan.org/docs/jinja2/templates.html#tests)

4. 注释
    
   `{# ... #}`
   
   * 要把模板中一行的部分注释掉，默认使用 {# ... #} 注释语法。
   ```
    {# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
    #}
    ```

## 关系

extends 继承

block 替换，依赖于我们继承

include 包含
