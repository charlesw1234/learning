import wx
import wx.xrc as xrc
from supply import SashLayoutWindowXmlHandler

class MyApp(wx.App):
    def OnInit(self):
        res = xrc.XmlResource_Get()
        res.AddHandler(SashLayoutWindowXmlHandler())
        print(res.LoadFile('tsashwin.xrc'))
        frame = res.LoadFrame(None, 'TestSashFrame')
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()
