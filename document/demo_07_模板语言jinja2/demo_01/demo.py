# from jinja2 import Template
#
# template = Template('Hello {{ name }}!')
# render_html1 = template.render(name='John Doe')
# print(render_html1)
# render_html2 = template.render({'name': 'ten'})
# print(render_html2)


# from jinja2 import Environment, PackageLoader
#
# env = Environment(loader=PackageLoader(__name__, 'templates'))
# """
# 这会创建一个默认设定下的模板环境和一个在 yourapplication python 包中的 templates 文件夹中寻找模板的加载器。
# 多个加载器是可用的，如果你需要从 数据库或其它资源加载模板，你也可以自己写一个。
# 你只需要调用 get_template() 方法从这个环境中加载模板，并会返回已加载的 Template:
# """
# template = env.get_template('mytemplate.html')
# render_html1 = template.render(title='我是谁', content='我是ten老师')
# print(render_html1)

