from jinja2 import Environment, PackageLoader

env = Environment(loader = PackageLoader('try', 'templates'))
template = env.get_template('first.xrc')
print(template.render(val0 = 'val(0)', val1 = 'val(1)'))
