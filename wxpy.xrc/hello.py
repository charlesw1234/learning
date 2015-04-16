import wx
import wx.xrc as xrc

class MyApp(wx.App):
    def OnInit(self):
        res0 = xrc.XmlResource('hello0.xrc')
        res1 = xrc.XmlResource('hello1.xrc')
        frame = res0.LoadFrame(None, 'MyFrame0')
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp(redirect = True)
app.MainLoop()
