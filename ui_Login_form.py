# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_formVuMltX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_slider = QFrame(self.centralwidget)
        self.login_slider.setObjectName(u"login_slider")
        self.login_slider.setMinimumSize(QSize(300, 0))
        self.login_slider.setMaximumSize(QSize(310, 16777215))
        self.login_slider.setStyleSheet(u"background-color: None;")
        self.login_slider.setFrameShape(QFrame.StyledPanel)
        self.login_slider.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.login_slider)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_holder = QFrame(self.login_slider)
        self.name_holder.setObjectName(u"name_holder")
        self.name_holder.setMinimumSize(QSize(290, 0))
        self.name_holder.setStyleSheet(u"background-color: rgb(34, 45, 61);\n"
"\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.name_holder.setFrameShape(QFrame.StyledPanel)
        self.name_holder.setFrameShadow(QFrame.Raised)
        self.plainTextEdit_3 = QPlainTextEdit(self.name_holder)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(70, 280, 191, 41))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setAcceptDrops(False)
        self.plainTextEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_4 = QPlainTextEdit(self.name_holder)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(60, 490, 211, 41))
        font1 = QFont()
        font1.setFamily(u"Century Gothic")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.plainTextEdit_4.setFont(font1)
        self.plainTextEdit_4.setStyleSheet(u"\n"
"\n"
"color: rgb(232, 140, 48);\n"
"background-color: rgba(255, 255, 255,0);")
        self.plainTextEdit_4.setReadOnly(True)
        self.pushButton_3 = QPushButton(self.name_holder)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 380, 151, 111))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	image: url(:/prefix/icons/500-fingerprint-security-outline.png);\n"
"background-color:rgba(255,255,255,0);\n"
"	image: url(:/prefix/icons/500-fingerprint-security-outline.png);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/500-fingerprint-security-outline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(120, 120))
        self.frame_2 = QFrame(self.name_holder)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 40, 301, 261))
        self.frame_2.setStyleSheet(u"image: url(:/prefix/icons/403-museum-authority-outline.svg);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Minimize = QPushButton(self.name_holder)
        self.Minimize.setObjectName(u"Minimize")
        self.Minimize.setGeometry(QRect(240, 10, 16, 16))
        self.Minimize.setStyleSheet(u"QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(255, 95, 88);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(136, 47, 232);\n"
"\n"
"}")
        self.Close = QPushButton(self.name_holder)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(260, 10, 16, 16))
        self.Close.setStyleSheet(u"QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(42, 201, 63);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(136, 47, 232);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.name_holder)

        self.login_form = QFrame(self.login_slider)
        self.login_form.setObjectName(u"login_form")
        self.login_form.setMaximumSize(QSize(16777215, 500))
        self.login_form.setStyleSheet(u"background-color: rgb(67, 82, 104);\n"
"\n"
"border-radius:10px;")
        self.login_form.setFrameShape(QFrame.StyledPanel)
        self.login_form.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.login_form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(30, 250, 221, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 100))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 200))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.username.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Georgia")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.username.setFont(font2)
        self.username.setStyleSheet(u"\n"
"QLineEdit\n"
"{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(160, 197, 248);\n"
"\n"
"color: rgba(255,255,255,100);\n"
"padding-bottom: 7px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgba(163, 163, 163, 50);\n"
"\n"
"}\n"
"")
        self.username.setEchoMode(QLineEdit.Normal)
        self.username.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.pushButton_2 = QPushButton(self.login_form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 430, 221, 40))
        palette1 = QPalette()
        brush5 = QBrush(QColor(34, 45, 61, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        brush6 = QBrush(QColor(120, 120, 120, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.pushButton_2.setPalette(palette1)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(34, 45, 61);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: rgb(255,255,255);\n"
"	\n"
"	background-color: rgb(232, 140, 48);\n"
"\n"
"\n"
"\n"
"border:2px solid rgba(0,0,0,50);\n"
"\n"
"}\n"
"")
        self.frame = QFrame(self.login_form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 271, 181))
        self.frame.setStyleSheet(u"image: url(:/prefix/icons/21-avatar-outline.png);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.plainTextEdit_2 = QPlainTextEdit(self.login_form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(50, 180, 221, 41))
        font3 = QFont()
        font3.setFamily(u"Century Gothic")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.plainTextEdit_2.setFont(font3)
        self.plainTextEdit_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);")
        self.password = QLineEdit(self.login_form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(30, 330, 221, 41))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.password.setPalette(palette2)
        self.password.setFont(font2)
        self.password.setStyleSheet(u"\n"
"QLineEdit\n"
"{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(160, 197, 248);\n"
"\n"
"color: rgba(255,255,255,100);\n"
"padding-bottom: 7px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgba(163, 163, 163, 50);\n"
"\n"
"}\n"
"")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.login_fail = QLineEdit(self.login_form)
        self.login_fail.setObjectName(u"login_fail")
        self.login_fail.setGeometry(QRect(30, 390, 271, 31))
        font4 = QFont()
        font4.setPointSize(9)
        self.login_fail.setFont(font4)
        self.login_fail.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.login_form)


        self.horizontalLayout.addWidget(self.login_slider)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"My Industry", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"Authenticate yourself", None))
        self.pushButton_3.setText("")
        self.Minimize.setText("")
        self.Close.setText("")
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Authentication Hub", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_fail.setText("")
    # retranslateUi

