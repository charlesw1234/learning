import wx
import wx.xrc as xrc

def DumpWidgetTree(prefix, widget):
    print('%s%s@%s' % (prefix, repr(widget), repr(widget.GetClientSize())))
    for subwidget in widget.GetChildren():
        DumpWidgetTree(prefix + '  ', subwidget)

class SashPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.remainingSpace = None

    def SetRemainingSpace(self, subwin):
        if self.remainingSpace is not None:
            print('More then one remaing space is not permitted.')
        self.remainingSpace = subwin

    def OnSashDrag(self, event):
        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            print('drag is out of range')
            return
        eobj = event.GetEventObject()
        if isinstance(eobj, wx.SashLayoutWindow):
            print('event.GetDragRect()', event.GetDragRect().GetSize())
            eobj.SetDefaultSize(event.GetDragRect().GetSize())
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
            sashpanel.Create(self.GetParentAsWindow(),
                             self.GetID(),
                             self.GetPosition(),
                             self.GetSize(),
                             self.GetStyle(),
                             self.GetName())
        self.SetupWindow(sashpanel)
        self.CreateChildren(sashpanel)
        for subwin in sashpanel.GetChildren():
            if not isinstance(subwin, wx.SashLayoutWindow):
                sashpanel.SetRemainingSpace(subwin)
            else:
                sashpanel.Bind(wx.EVT_SASH_DRAGGED_RANGE,
                               sashpanel.OnSashDrag,
                               id = subwin.GetId())
        sashpanel.Bind(wx.EVT_SIZE, sashpanel.OnSize)
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
        if self.GetInstance() is None:
            sashwin = wx.SashLayoutWindow(self.GetParentAsWindow(),
                                          self.GetID(),
                                          self.GetPosition(),
                                          self.GetSize(),
                                          self.GetStyle("flag"),
                                          self.GetName())
        else:
            sashwin = self.GetInstance()
            sashwin.Create(self.GetParentAsWindow(),
                           self.GetID(),
                           self.GetPosition(),
                           self.GetSize(),
                           self.GetStyle("flag"),
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
        if self.HasParam("background"):
            background = self.GetColour("background")
            sashwin.SetBackgroundColour(background)
        if self.HasParam("defaultsize"):
            defaultsize = self.GetSize("defaultsize")
            sashwin.SetDefaultSize(defaultsize)
        if self.HasParam("extrabordersize"):
            extrabordersize = self.GetLong("extrabordersize")
            sashwin.SetExtraBorderSize(extrabordersize)
        self.CreateChildren(sashwin)
        return sashwin
