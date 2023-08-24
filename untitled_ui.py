# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"color: rgb(0, 60, 69);\n"
"background-color: rgb(173, 219, 227);")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 60, 141, 51))
        self.pushButton.setStyleSheet(u"border-image: url(:/png/res/image/Blue_Buttons_Round_Edge_small.png);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 30, 81, 16))
        self.graphicsView = QChartView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(260, 60, 471, 351))
        self.graphicsView.setStyleSheet(u"background-color: rgb(0, 170, 144);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 130, 141, 41))
        self.pushButton_2.setStyleSheet(u"border-image: url(:/png/res/image/menu_btn_press.png);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 450, 91, 91))
        self.label_2.setStyleSheet(u"image: url(:/png/res/image/compass.png);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(600, 30, 133, 21))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 30, 61, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 230, 161, 71))
        self.label_4.setStyleSheet(u"border-image: url(:/png/res/image/g03_can_box_red.png);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 340, 164, 74))
        self.pushButton_3.setStyleSheet(u"border-image: url(:/png/res/image/g02_can_box_green.png);")
        self.pushButton_3.setIconSize(QSize(16, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuFIle.addAction(self.actionQuit)
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.slot2)
        self.action.triggered.connect(MainWindow.slot3)
        self.pushButton.clicked.connect(MainWindow.slot1)
        self.pushButton_2.clicked.connect(MainWindow.slot4)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u66f2\u7ebf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello pyside\uff01", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.label_2.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"360.00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8f6c\u901f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

