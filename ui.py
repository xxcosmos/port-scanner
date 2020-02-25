# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PortScanUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 521, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.network_a = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.network_a.setObjectName("network_a")
        self.gridLayout.addWidget(self.network_a, 2, 2, 1, 1)
        self.network_b = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.network_b.setObjectName("network_b")
        self.gridLayout.addWidget(self.network_b, 2, 4, 1, 1)
        self.network_c = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.network_c.setObjectName("network_c")
        self.gridLayout.addWidget(self.network_c, 2, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout_2.addWidget(self.stop_button, 2, 4, 1, 1)
        self.host_b = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.host_b.setObjectName("host_b")
        self.gridLayout_2.addWidget(self.host_b, 0, 4, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scan_times = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.scan_times.setPrefix("")
        self.scan_times.setMinimum(1)
        self.scan_times.setMaximum(4)
        self.scan_times.setSingleStep(1)
        self.scan_times.setObjectName("scan_times")
        self.gridLayout_3.addWidget(self.scan_times, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.timeout = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.timeout.setProperty("showGroupSeparator", False)
        self.timeout.setDecimals(1)
        self.timeout.setMinimum(0.1)
        self.timeout.setMaximum(3.0)
        self.timeout.setSingleStep(0.1)
        self.timeout.setObjectName("timeout")
        self.gridLayout_3.addWidget(self.timeout, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.host_a = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.host_a.setClearButtonEnabled(False)
        self.host_a.setObjectName("host_a")
        self.gridLayout_2.addWidget(self.host_a, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.start_button.setAutoDefault(False)
        self.start_button.setDefault(False)
        self.start_button.setFlat(False)
        self.start_button.setObjectName("start_button")
        self.gridLayout_2.addWidget(self.start_button, 2, 1, 1, 1)
        self.port_b = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.port_b.setObjectName("port_b")
        self.gridLayout_2.addWidget(self.port_b, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.port_a = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.port_a.setObjectName("port_a")
        self.gridLayout_2.addWidget(self.port_a, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 33)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.progress_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayout.addWidget(self.progress_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.result = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.result.setGeometry(QtCore.QRect(0, -10, 521, 301))
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "端口扫描"))
        self.network_a.setText(_translate("MainWindow", "192"))
        self.network_b.setText(_translate("MainWindow", "168"))
        self.network_c.setText(_translate("MainWindow", "123"))
        self.label_3.setText(_translate("MainWindow", "."))
        self.label.setText(_translate("MainWindow", "网络号："))
        self.label_2.setText(_translate("MainWindow", "."))
        self.stop_button.setText(_translate("MainWindow", "停止"))
        self.host_b.setText(_translate("MainWindow", "254"))
        self.scan_times.setSuffix(_translate("MainWindow", " 次"))
        self.label_8.setText(_translate("MainWindow", "扫描次数："))
        self.label_9.setText(_translate("MainWindow", "超时："))
        self.timeout.setSuffix(_translate("MainWindow", " 秒"))
        self.label_4.setText(_translate("MainWindow", "主机范围：（1～254）"))
        self.label_7.setText(_translate("MainWindow", "～"))
        self.host_a.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "端口范围：（0～65535）"))
        self.start_button.setText(_translate("MainWindow", "开始"))
        self.port_b.setText(_translate("MainWindow", "1024"))
        self.label_5.setText(_translate("MainWindow", "～"))
        self.port_a.setText(_translate("MainWindow", "0"))
        self.progress_label.setText(_translate("MainWindow", "0 %"))
        self.result.setDocumentTitle(_translate("MainWindow", "结果"))