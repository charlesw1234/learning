import wx
import wx.xrc as xrc

class MyApp(wx.App):
    def OnInit(self):
        res = xrc.XmlResource_Get()
        res.LoadFile('hello0.xrc')
        res.LoadFile('hello1.xrc')
        res0 = xrc.EmptyXmlResource()
        print('try.xrc', res0.LoadFromString(open('try.xrc', 'rt').read()))
        print('first', res.GetResourceNode('first'),
              res0.GetResourceNode('first'))
        return False

app = MyApp()
app.MainLoop()
