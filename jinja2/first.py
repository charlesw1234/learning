from jinja2 import Environment, PackageLoader

class autogen(dict):
    def __init__(self):
        self.values = [{ 'a': 'VAL0A', 'b': 'VAL0B' },
                       { 'a': 'VAL1A', 'b': 'VAL1B' }]

    def upperit(self, name):
        return name.upper()

env = Environment(loader = PackageLoader('try', 'templates'))
template = env.get_template('first.xrc')
print(template.render(agobj = autogen()))
