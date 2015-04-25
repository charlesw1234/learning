import wx.xrc as xrc

class SashLayoutWindowXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        #self.AddStyle("wx???", wx.???)
        self.AddWindowStyles()

    def CanHandle(self, node):
        return self.IsOfClass(node, "SashLayoutWindow")

    def DoCreateResource(self):
        if self.GetInstance() is None:
            sashwin = wx.SashLayoutWindow(self.GetParentAsWindow(),
                                          self.GetID(),
                                          self.GetPosition(),
                                          self.GetSize(),
                                          self.GetStyle(),
                                          self.GetName())
        else:
            sashwin = self.GetInstance()
            if sashwin is None: sashwin = wx.PreSashLayoutWindow()
            sashwin.Create(self.GetParentAsWindow(),
                           self.GetID(),
                           self.GetPosition(),
                           self.GetSize(),
                           self.GetStyle(),
                           self.GetName())
        self.SetupWindow(sashwin)
        self.CreateChildren(sashwin)
        return sashwin
