import wx
import wx.xrc as xrc
import wx.dataview as dv

class TestModel(dv.PyDataViewIndexListModel):
    def __init__(self, data):
        dv.PyDataViewIndexListModel.__init__(self, len(data))
        self.data = data

    def GetColumnType(self, col):
        return 'string'

    def GetValueByRow(self, row, col):
        return self.data[row][col - 1]

    def SetValueByRow(self, value, row, col):
        self.data[row][col] = value

    def GetColumnCount(self):
        return len(self.data[0])

    def GetCount(self):
        return len(self.data)

    def GetAttrByRow(self, row, col, attr):
        print(row, col, attr, dir(attr))
        return False

    def Compare(self, item1, item2, col, ascending):
        if not ascending: item2, item1 = item1, item2
        row1 = self.GetRow(item1)
        row2 = self.GetRow(item2)
        return cmp(self.data[row1][col], self.data[row2][col])

    def DeleteRows(self, rows):
        rows = list(rows)
        rows.sort(reverse = True)
        for row in rows:
            del(self.data[row])
            self.RowDeleted(row)

    def AddRow(self, value):
        self.data.append(value)
        self.RowAppended()

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.dvc = dv.DataViewCtrl(self, style = wx.BORDER_THEME | dv.DV_ROW_LINES | dv.DV_VERT_RULES | dv.DV_MULTIPLE)
        self.dvc.AppendTextColumn('Artist', 1, width = 170)
        self.dvc.AppendTextColumn('Title', 2, width = 260)
        self.dvc.AppendTextColumn('Genre', 3, width = 80)
        for col in self.dvc.Columns:
            col.Sortable = True
            col.Reorderable = True
        self.model = TestModel([['yes', 'YES', 'Yes'],
                                ['no', 'NO', 'No']])
        self.dvc.AssociateModel(self.model)
        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.dvc, 1, wx.EXPAND)
        #self.SetSizer(self.sizer)

class MyApp(wx.App):
    def OnInit(self):
        #res = xrc.XmlResource_Get()
        #res.LoadFile('tdv.xrc')
        frame = wx.Frame(None)
        TestPanel(frame)
        self.SetTopWindow(frame)
        frame.Fit()
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()
