import wx
import wx.xrc as xrc

def DumpWidgetTree(prefix, widget):
    print('%s%s@%s' % (prefix, repr(widget), repr(widget.GetClientSize())))
    for subwidget in widget.GetChildren():
        DumpWidgetTree(prefix + '  ', subwidget)

class SashPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

    def OnSashDrag(self, event):
        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            print('drag is out of range')
            return
        eobj = event.GetEventObject()
        if isinstance(eobj, wx.SashLayoutWindow):
            eobj.SetDefaultSize((eobj.GetSize().width,
                                 event.GetDragRect().height))
        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        self.remainingSpace.Refresh()

    def OnSize(self, event):
        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)

class SashPanelXmlHandler(xrc.XmlResourceHandler):
    def CanHandle(self, node):
        return self.IsOfClass(node, 'SashPanel')

    def DoCreateResource(self):
        if self.GetInstance() is None:
            sashpanel = SashPanel(self.GetParentAsWindow(),
                                  self.GetID(),
                                  self.GetPosition(),
                                  self.GetSize(),
                                  self.GetStyle(),
                                  self.GetName())
        else:
            sashpanel = self.GetInstance()
            if sashpanel is None: sashpanel = wx.SashPanel()
            sashpanel.Create(self.GetParentAsWindow(),
                             self.GetID(),
                             self.GetPosition(),
                             self.GetSize(),
                             self.GetStyle(),
                             self.GetName())
        self.SetupWindow(sashpanel)
        self.CreateChildren(sashpanel)
        return sashpanel

class wxSashLayoutWindowXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        self.AddStyle("wxSW_NOBORDER", wx.SW_NOBORDER)
        self.AddStyle("wxSW_BORDER", wx.SW_BORDER)
        self.AddStyle("wxSW_3DSASH", wx.SW_3DSASH)
        self.AddStyle("wxSW_3DBORDER", wx.SW_3DBORDER)
        self.AddStyle("wxSW_3D", wx.SW_3D)
        self.AddStyle("wxLAYOUT_HORIZONTAL", wx.LAYOUT_HORIZONTAL)
        self.AddStyle("wxLAYOUT_VERTICAL", wx.LAYOUT_VERTICAL)
        self.AddStyle("wxLAYOUT_TOP", wx.LAYOUT_TOP)
        self.AddStyle("wxLAYOUT_BOTTOM", wx.LAYOUT_BOTTOM)
        self.AddStyle("wxLAYOUT_LEFT", wx.LAYOUT_LEFT)
        self.AddStyle("wxLAYOUT_RIGHT", wx.LAYOUT_RIGHT)
        self.AddStyle("wxSASH_NONE", wx.SASH_NONE)
        self.AddStyle("wxSASH_TOP", wx.SASH_TOP)
        self.AddStyle("wxSASH_BOTTOM", wx.SASH_BOTTOM)
        self.AddStyle("wxSASH_LEFT", wx.SASH_LEFT)
        self.AddStyle("wxSASH_RIGHT", wx.SASH_RIGHT)
        self.AddWindowStyles()

    def CanHandle(self, node):
        return self.IsOfClass(node, "wxSashLayoutWindow")

    def DoCreateResource(self):
        print('DoCreateResource', self.GetSize(), self.GetStyle())
        if self.GetInstance() is None:
            sashwin = wx.SashLayoutWindow(self.GetParentAsWindow(),
                                          self.GetID(),
                                          self.GetPosition(),
                                          (200, 30),
                                          #self.GetSize(),
                                          self.GetStyle(),
                                          self.GetName())
        else:
            sashwin = self.GetInstance()
            if sashwin is None: sashwin = wx.PreSashLayoutWindow()
            sashwin.Create(self.GetParentAsWindow(),
                           self.GetID(),
                           self.GetPosition(),
                           (200, 30),
                           #self.GetSize(),
                           self.GetStyle(),
                           self.GetName())
        self.SetupWindow(sashwin)
        if self.HasParam("orientation"):
            orient = self.GetStyle("orientation", wx.LAYOUT_VERTICAL)
            sashwin.SetOrientation(orient)
        if self.HasParam("alignment"):
            alignment = self.GetStyle("alignment", wx.LAYOUT_TOP)
            sashwin.SetAlignment(alignment)
        if self.HasParam("sashvisible"):
            sashvisible = self.GetStyle("sashvisible", wx.SASH_NONE)
            sashwin.SetSashVisible(sashvisible, True)
        sashwin.SetDefaultSize((800, 96))
        self.CreateChildren(sashwin)
        return sashwin
