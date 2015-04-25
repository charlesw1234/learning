from jinja2 import Environment, PackageLoader

class autogen(dict):
    def __init__(self):
        self.values = [{ 'a': 'VAL0A', 'b': 'VAL0B' },
                       { 'a': 'VAL1A', 'b': 'VAL1B' }]

    def upperit(self, name):
        return name.upper()

    def lowerit(self, name):
        return name.lower()

    def sideeffect(self, name):
        print(name.upper(), name.lower())

print('A(0)')
env = Environment(loader = PackageLoader('try', 'templates'))
print('A(1)')
template = env.get_template('first.xrc')
print('A(2)')
print(template.render(agobj = autogen()))
