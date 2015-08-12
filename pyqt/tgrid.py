import sys
from PyQt4 import QtGui, QtCore

class GridFrame(QtGui.QFrame):
    def __init__(self, *args, **kwargs):
        super(GridFrame, self).__init__(*args, **kwargs)
        layout = QtGui.QGridLayout()
        for row in range(5):
            if row % 2 == 0:
                for col in range(2):
                    title = '(%u,%u)' % (row, col)
                    #frame = QtGui.QFrame(self)
                    #frame.setFrameShape(QtGui.QFrame.StyledPanel)
                    #QtGui.QLabel(title, frame)
                    #layout.addWidget(frame, row, col)
                    layout.addWidget(QtGui.QLabel(title, self), row, col)
            else:
                shobj = QtGui.QSplitterHandle(QtCore.Qt.Horizontal, self)
                layout.addWidget(shobj, row, col, 1, 2)
        self.setLayout(layout)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        grid = GridFrame(self)
        self.setCentralWidget(grid)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName('tgrid')
    app.setOrganizationDomain('tgrid.com')
    app.setApplicationName('tgrid tester')
    mainwin = MainWindow()
    mainwin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
