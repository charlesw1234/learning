import wx
import wx.xrc as xrc

class MyApp(wx.App):
    def OnInit(self):
        #res0 = xrc.XmlResource('hello0.xrc')
        #print('res0 = %s\n' % res0)
        #res1 = xrc.XmlResource('hello1.xrc')
        #print('res1 = %s\n' % res1)
        res = xrc.XmlResource_Get()
        print('res = %s' % res)
        print(res.LoadFile('hello0.xrc'))
        print(res.LoadFile('hello1.xrc'))
        frame = res.LoadFrame(None, 'MyFrame0')
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp()
#app = MyApp(redirect = True)
app.MainLoop()
