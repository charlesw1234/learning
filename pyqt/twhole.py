import sys
from PyQt4 import QtGui, QtCore

class MdiArea(QtGui.QMdiArea):
    def __init__(self):
        super(MdiArea, self).__init__()
        self.initSubWindows()

    def initSubWindows(self):
        self.makeSubWindow('First')
        self.makeSubWindow('Second')
        self.makeSubWindow('Third')

    def makeSubWindow(self, title):
        subwin = QtGui.QMdiSubWindow()
        subwin.setWidget(QtGui.QLabel(title))
        subwin.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.addSubWindow(subwin)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.createActions()
        self.createMenus()
        self.initUI()

    def createActions(self):
        setattr(self, 'saveLayoutAct',
                QtGui.QAction(QtGui.QIcon(':/images/save.png'), '&Save', self,
                              statusTip = 'Save the current layout',
                              triggered = self.saveLayout))
        setattr(self, 'loadLayoutAct',
                QtGui.QAction(QtGui.QIcon(':/images/load.png'), '&Load', self,
                              statusTip = 'Load the saved layout',
                              triggered = self.loadLayout))

    def createMenus(self):
        self.layoutMenu = self.menuBar().addMenu('&Layout')
        self.layoutMenu.addAction(self.saveLayoutAct)
        self.layoutMenu.addAction(self.loadLayoutAct)

    def initUI(self):
        mdiarea = MdiArea()
        self.setCentralWidget(mdiarea)
        self.makeDock('first', QtCore.Qt.LeftDockWidgetArea,
                      QtCore.Qt.LeftDockWidgetArea)
        self.makeDock('second', QtCore.Qt.RightDockWidgetArea,
                      QtCore.Qt.RightDockWidgetArea)
        self.makeDock('third', QtCore.Qt.RightDockWidgetArea,
                      QtCore.Qt.RightDockWidgetArea)
        self.statusBar().showMessage('Ready')

    def makeDock(self, title, located, allowed):
        dock = QtGui.QDockWidget(title, self)
        dock.setObjectName(title)
        dock.setAllowedAreas(allowed)
        frame = QtGui.QFrame(self)
        frame.setFrameShape(QtGui.QFrame.StyledPanel)
        dock.setWidget(frame)
        self.addDockWidget(located, dock)

    def saveLayout(self):
        settings = QtCore.QSettings()
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('state', self.saveState())
        print('saveLayout', settings.fileName())

    def loadLayout(self):
        settings = QtCore.QSettings()
        self.restoreGeometry(settings.value('geometry').toByteArray())
        self.restoreState(settings.value('state').toByteArray())
        print('loadLayout', settings.fileName())

def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName('twhole')
    app.setOrganizationDomain('twhole.com')
    app.setApplicationName('twhole tester')
    mainwin = MainWindow()
    mainwin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
