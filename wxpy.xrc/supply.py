import wx
import wx.xrc as xrc

class SashLayoutWindowXmlHandler(xrc.XmlResourceHandler):
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
        if self.HasParam("orientation"):
            orient = self.GetStyle("orientation", wx.LAYOUT_VERTICAL)
            sashwin.SetOrientation(orient)
        if self.HasParam("alignment"):
            alignment = self.GetStyle("alignment", wx.LAYOUT_TOP)
            sashwin.SetAlignment(alignment)
        if self.HasParam("sashvisible"):
            sashvisible = self.GetStyle("sashvisible", wx.SASH_NONE)
            sashwin.SetSashVisible(sashvisible, True)
        self.CreateChildren(sashwin)
        return sashwin
