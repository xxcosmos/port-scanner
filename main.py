import sys

from PyQt5 import QtWidgets

from ui_process import PortScanner

# 主程序入口
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = PortScanner()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
