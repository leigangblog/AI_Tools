import sys
import main_func
from PyQt5 import QtWidgets, QtGui, QtCore
import time
debug = 1

def main():
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/images/demo1.png"))
    splash.showMessage("正在初始化程序...", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()
    time.sleep(3)
    QtWidgets.qApp.processEvents()
    if debug:
        ui = main_func.QmyMainWindow()
        ui.showMaximized()
        ui.show()
        splash.finish(ui)
    else:
        return

    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
