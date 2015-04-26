import wx
import wx.xrc as xrc
from supply import DumpWidgetTree, wxSashLayoutWindowXmlHandler

class MyApp(wx.App):
    def OnInit(self):
        res = xrc.XmlResource_Get()
        res.AddHandler(wxSashLayoutWindowXmlHandler())
        print(res.LoadFile('tsashwin.xrc'))
        frame = res.LoadFrame(None, 'TestSashFrame')
        self.SetTopWindow(frame)
        frame.Fit()
        frame.Show(True)
        DumpWidgetTree('frame:', frame)
        return True

app = MyApp()
app.MainLoop()
