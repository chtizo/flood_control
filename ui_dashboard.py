# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardfxlTBa.ui'
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

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1520, 990)
        Dashboard.setStyleSheet(u"background-color:rgb(255,255,255)")
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1520, 990))
        self.frame.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(26, 34, 47);\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Close = QPushButton(self.frame)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(1440, 15, 16, 16))
        self.Close.setStyleSheet(u"QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(255, 95, 88);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(136, 47, 232);\n"
"\n"
"}")
        self.Minimize = QPushButton(self.frame)
        self.Minimize.setObjectName(u"Minimize")
        self.Minimize.setGeometry(QRect(1480, 15, 16, 16))
        self.Minimize.setStyleSheet(u"QPushButton{\n"
"border-radius: 7px;\n"
"background-color: rgb(42, 201, 63);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(136, 47, 232);\n"
"\n"
"}\n"
"")
        self.FlowrateBG = QFrame(self.frame)
        self.FlowrateBG.setObjectName(u"FlowrateBG")
        self.FlowrateBG.setEnabled(False)
        self.FlowrateBG.setGeometry(QRect(90, 90, 241, 241))
        self.FlowrateBG.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:None;\n"
"}")
        self.FlowrateBG.setFrameShape(QFrame.NoFrame)
        self.FlowrateBG.setFrameShadow(QFrame.Raised)
        self.FlowrateProgressBar = QFrame(self.FlowrateBG)
        self.FlowrateProgressBar.setObjectName(u"FlowrateProgressBar")
        self.FlowrateProgressBar.setEnabled(False)
        self.FlowrateProgressBar.setGeometry(QRect(10, 10, 221, 221))
        self.FlowrateProgressBar.setStyleSheet(u"QFrame{\n"
"	\n"
"border-radius: 110px;\n"
"	\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"    \n"
"	\n"
"}")
        self.FlowrateProgressBar.setFrameShape(QFrame.NoFrame)
        self.FlowrateProgressBar.setFrameShadow(QFrame.Raised)
        self.Flowrate_container = QFrame(self.FlowrateProgressBar)
        self.Flowrate_container.setObjectName(u"Flowrate_container")
        self.Flowrate_container.setGeometry(QRect(10, 10, 200, 200))
        self.Flowrate_container.setStyleSheet(u"QFrame\n"
"{\n"
"border-radius: 100px;\n"
"	background-color: rgb(24, 32, 43);\n"
"}")
        self.Flowrate_container.setFrameShape(QFrame.NoFrame)
        self.Flowrate_container.setFrameShadow(QFrame.Raised)
        self.icon_holder = QFrame(self.Flowrate_container)
        self.icon_holder.setObjectName(u"icon_holder")
        self.icon_holder.setGeometry(QRect(47, 44, 110, 110))
        self.icon_holder.setStyleSheet(u"image: url(:/prefix/icons/wind.png);\n"
"background-color:transparent;\n"
"")
        self.icon_holder.setFrameShape(QFrame.StyledPanel)
        self.icon_holder.setFrameShadow(QFrame.Raised)
        self.Flowrate_level = QFrame(self.FlowrateBG)
        self.Flowrate_level.setObjectName(u"Flowrate_level")
        self.Flowrate_level.setEnabled(False)
        self.Flowrate_level.setGeometry(QRect(5, 5, 230, 230))
        self.Flowrate_level.setStyleSheet(u"\n"
"QFrame\n"
"{\n"
"border-radius: 115px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(0, 255, 251, 0), stop:0.749 rgba(255, 148, 0, 0));\n"
"	\n"
"	\n"
"}")
        self.Flowrate_level.setFrameShape(QFrame.NoFrame)
        self.Flowrate_level.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.Flowrate_level)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(4, 4, 221, 221))
        font = QFont()
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"QFrame\n"
"{\n"
"    border-radius: 110px;\n"
"	background-color: rgba(165, 144, 174,150);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Flowrate_level.raise_()
        self.FlowrateProgressBar.raise_()
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(590, 20, 31, 31))
        self.frame_5.setStyleSheet(u"image: url(:/prefix/wifi_inapp.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.Flowrate_holder = QFrame(self.frame)
        self.Flowrate_holder.setObjectName(u"Flowrate_holder")
        self.Flowrate_holder.setGeometry(QRect(50, 80, 521, 251))
        self.Flowrate_holder.setAutoFillBackground(False)
        self.Flowrate_holder.setStyleSheet(u"\n"
"\n"
"\n"
"background-color: rgba(136, 190, 240,0.14);\n"
"\n"
"\n"
"\n"
"border-radius: 50%;\n"
"")
        self.Flowrate_holder.setFrameShape(QFrame.StyledPanel)
        self.Flowrate_holder.setFrameShadow(QFrame.Raised)
        self.Flowrate_holder.setLineWidth(3)
        self.Flowrate_holder.setMidLineWidth(3)
        self.Flowrate = QLabel(self.Flowrate_holder)
        self.Flowrate.setObjectName(u"Flowrate")
        self.Flowrate.setGeometry(QRect(317, 90, 131, 91))
        font1 = QFont()
        font1.setFamily(u"Rockwell")
        font1.setPointSize(50)
        self.Flowrate.setFont(font1)
        self.Flowrate.setStyleSheet(u"color: #ffffff;\n"
"background-color:None;\n"
"")
        self.Flowrate.setAlignment(Qt.AlignCenter)
        self.LPM = QLabel(self.Flowrate_holder)
        self.LPM.setObjectName(u"LPM")
        self.LPM.setGeometry(QRect(326, 180, 81, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.LPM.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.LPM.setFont(font2)
        self.LPM.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(255,255,255);")
        self.Flowrate_label = QLineEdit(self.Flowrate_holder)
        self.Flowrate_label.setObjectName(u"Flowrate_label")
        self.Flowrate_label.setGeometry(QRect(290, 40, 201, 51))
        font3 = QFont()
        font3.setFamily(u"Rockwell")
        self.Flowrate_label.setFont(font3)
        self.Flowrate_label.setStyleSheet(u"color: white;\n"
"font-size: 30px;\n"
"background-color: rgba(0,0,0,0);")
        self.Flowrate_label.setAlignment(Qt.AlignCenter)
        self.Flowratedial_shadow = QFrame(self.Flowrate_holder)
        self.Flowratedial_shadow.setObjectName(u"Flowratedial_shadow")
        self.Flowratedial_shadow.setEnabled(False)
        self.Flowratedial_shadow.setGeometry(QRect(49, 18, 230, 230))
        self.Flowratedial_shadow.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:rgba(0,0,0,0.1);\n"
"border-radius:110%;\n"
"}")
        self.Flowratedial_shadow.setFrameShape(QFrame.NoFrame)
        self.Flowratedial_shadow.setFrameShadow(QFrame.Raised)
        self.Flowratedial_shadow.raise_()
        self.Flowrate.raise_()
        self.LPM.raise_()
        self.Flowrate_label.raise_()
        self.WaterlevelBG = QFrame(self.frame)
        self.WaterlevelBG.setObjectName(u"WaterlevelBG")
        self.WaterlevelBG.setEnabled(False)
        self.WaterlevelBG.setGeometry(QRect(650, 89, 241, 241))
        self.WaterlevelBG.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:None;\n"
"}")
        self.WaterlevelBG.setFrameShape(QFrame.NoFrame)
        self.WaterlevelBG.setFrameShadow(QFrame.Raised)
        self.WaterlevelProgressBar = QFrame(self.WaterlevelBG)
        self.WaterlevelProgressBar.setObjectName(u"WaterlevelProgressBar")
        self.WaterlevelProgressBar.setEnabled(False)
        self.WaterlevelProgressBar.setGeometry(QRect(10, 10, 221, 221))
        self.WaterlevelProgressBar.setStyleSheet(u"QFrame{\n"
"	\n"
"border-radius: 110px;\n"
"	\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"    \n"
"	\n"
"}")
        self.WaterlevelProgressBar.setFrameShape(QFrame.NoFrame)
        self.WaterlevelProgressBar.setFrameShadow(QFrame.Raised)
        self.Waterlevel_container = QFrame(self.WaterlevelProgressBar)
        self.Waterlevel_container.setObjectName(u"Waterlevel_container")
        self.Waterlevel_container.setGeometry(QRect(10, 10, 200, 200))
        self.Waterlevel_container.setStyleSheet(u"QFrame\n"
"{\n"
"border-radius: 100px;\n"
"	background-color: rgb(24, 32, 43);\n"
"}")
        self.Waterlevel_container.setFrameShape(QFrame.NoFrame)
        self.Waterlevel_container.setFrameShadow(QFrame.Raised)
        self.Waterlevel_icon = QFrame(self.Waterlevel_container)
        self.Waterlevel_icon.setObjectName(u"Waterlevel_icon")
        self.Waterlevel_icon.setGeometry(QRect(45, 41, 110, 110))
        self.Waterlevel_icon.setStyleSheet(u"\n"
"image: url(:/prefix/icons/water-level.png);\n"
"background-color:transparent;\n"
"")
        self.Waterlevel_icon.setFrameShape(QFrame.StyledPanel)
        self.Waterlevel_icon.setFrameShadow(QFrame.Raised)
        self.Waterlevel_level_4 = QFrame(self.WaterlevelBG)
        self.Waterlevel_level_4.setObjectName(u"Waterlevel_level_4")
        self.Waterlevel_level_4.setEnabled(False)
        self.Waterlevel_level_4.setGeometry(QRect(5, 5, 230, 230))
        self.Waterlevel_level_4.setStyleSheet(u"\n"
"QFrame\n"
"{\n"
"border-radius: 115px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(0, 255, 251, 0), stop:0.75 rgba(255, 148, 0, 0));\n"
"	\n"
"	\n"
"}")
        self.Waterlevel_level_4.setFrameShape(QFrame.NoFrame)
        self.Waterlevel_level_4.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.Waterlevel_level_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(4, 4, 221, 221))
        self.frame_13.setFont(font)
        self.frame_13.setStyleSheet(u"QFrame\n"
"{\n"
"    border-radius: 110px;\n"
"	background-color: rgba(165, 144, 174,150);\n"
"}")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.Waterlevel_shadow = QFrame(self.WaterlevelBG)
        self.Waterlevel_shadow.setObjectName(u"Waterlevel_shadow")
        self.Waterlevel_shadow.setEnabled(False)
        self.Waterlevel_shadow.setGeometry(QRect(10, 10, 230, 230))
        self.Waterlevel_shadow.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:rgba(0,0,0,0.1);\n"
"border-radius:110px;\n"
"}")
        self.Waterlevel_shadow.setFrameShape(QFrame.NoFrame)
        self.Waterlevel_shadow.setFrameShadow(QFrame.Raised)
        self.Waterlevel_level_4.raise_()
        self.WaterlevelProgressBar.raise_()
        self.Waterlevel_shadow.raise_()
        self.Waterlevel_holder = QFrame(self.frame)
        self.Waterlevel_holder.setObjectName(u"Waterlevel_holder")
        self.Waterlevel_holder.setGeometry(QRect(610, 80, 521, 251))
        self.Waterlevel_holder.setStyleSheet(u"background-color: rgba(136, 190, 240,0.14);\n"
"border-radius: 50%;")
        self.Waterlevel_holder.setFrameShape(QFrame.StyledPanel)
        self.Waterlevel_holder.setFrameShadow(QFrame.Raised)
        self.Waterlevel = QLabel(self.Waterlevel_holder)
        self.Waterlevel.setObjectName(u"Waterlevel")
        self.Waterlevel.setGeometry(QRect(308, 90, 131, 91))
        self.Waterlevel.setFont(font1)
        self.Waterlevel.setStyleSheet(u"color: #ffffff;\n"
"background-color:None;\n"
"")
        self.Waterlevel.setAlignment(Qt.AlignCenter)
        self.cm = QLabel(self.Waterlevel_holder)
        self.cm.setObjectName(u"cm")
        self.cm.setGeometry(QRect(319, 180, 81, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.cm.setPalette(palette1)
        self.cm.setFont(font2)
        self.cm.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(255,255,255);")
        self.Waterlevel_label_2 = QLineEdit(self.Waterlevel_holder)
        self.Waterlevel_label_2.setObjectName(u"Waterlevel_label_2")
        self.Waterlevel_label_2.setGeometry(QRect(290, 40, 201, 51))
        self.Waterlevel_label_2.setFont(font3)
        self.Waterlevel_label_2.setStyleSheet(u"color: white;\n"
"font-size: 30px;\n"
"background-color: rgba(0,0,0,0);")
        self.Waterlevel_label_2.setAlignment(Qt.AlignCenter)
        self.cm.raise_()
        self.Waterlevel_label_2.raise_()
        self.Waterlevel.raise_()
        self.Flowrate_holder_shadow = QFrame(self.frame)
        self.Flowrate_holder_shadow.setObjectName(u"Flowrate_holder_shadow")
        self.Flowrate_holder_shadow.setGeometry(QRect(52, 81, 521, 251))
        self.Flowrate_holder_shadow.setAutoFillBackground(False)
        self.Flowrate_holder_shadow.setStyleSheet(u"background-color: rgba(0,0,0,0.1);\n"
"border-radius: 50%;\n"
"")
        self.Flowrate_holder_shadow.setFrameShape(QFrame.StyledPanel)
        self.Flowrate_holder_shadow.setFrameShadow(QFrame.Raised)
        self.Flowrate_holder_shadow.setLineWidth(3)
        self.Flowrate_holder_shadow.setMidLineWidth(3)
        self.Waterlevel_holder_shadow = QFrame(self.frame)
        self.Waterlevel_holder_shadow.setObjectName(u"Waterlevel_holder_shadow")
        self.Waterlevel_holder_shadow.setGeometry(QRect(612, 82, 521, 251))
        self.Waterlevel_holder_shadow.setAutoFillBackground(False)
        self.Waterlevel_holder_shadow.setStyleSheet(u"background-color: rgba(0,0,0,0.1);\n"
"border-radius: 50%;\n"
"")
        self.Waterlevel_holder_shadow.setFrameShape(QFrame.StyledPanel)
        self.Waterlevel_holder_shadow.setFrameShadow(QFrame.Raised)
        self.Waterlevel_holder_shadow.setLineWidth(3)
        self.Waterlevel_holder_shadow.setMidLineWidth(3)
        self.Temperature_holder = QFrame(self.frame)
        self.Temperature_holder.setObjectName(u"Temperature_holder")
        self.Temperature_holder.setGeometry(QRect(50, 380, 521, 191))
        self.Temperature_holder.setAutoFillBackground(False)
        self.Temperature_holder.setStyleSheet(u"\n"
"\n"
"\n"
"background-color: rgba(136, 190, 240,0.14);\n"
"\n"
"\n"
"\n"
"border-radius: 50%;\n"
"")
        self.Temperature_holder.setFrameShape(QFrame.StyledPanel)
        self.Temperature_holder.setFrameShadow(QFrame.Raised)
        self.Temperature_holder.setLineWidth(3)
        self.Temperature_holder.setMidLineWidth(3)
        self.Temperature = QLabel(self.Temperature_holder)
        self.Temperature.setObjectName(u"Temperature")
        self.Temperature.setGeometry(QRect(180, 80, 131, 91))
        font4 = QFont()
        font4.setFamily(u"Rockwell")
        font4.setPointSize(25)
        self.Temperature.setFont(font4)
        self.Temperature.setStyleSheet(u"color: #ffffff;\n"
"background-color:None;\n"
"")
        self.Temperature.setAlignment(Qt.AlignCenter)
        self.Temperature_label = QLineEdit(self.Temperature_holder)
        self.Temperature_label.setObjectName(u"Temperature_label")
        self.Temperature_label.setGeometry(QRect(200, 20, 201, 51))
        self.Temperature_label.setFont(font3)
        self.Temperature_label.setStyleSheet(u"color: white;\n"
"font-size: 30px;\n"
"background-color: rgba(0,0,0,0);")
        self.Temperature_label.setAlignment(Qt.AlignCenter)
        self.Temperature_icon_holder_shadow = QFrame(self.Temperature_holder)
        self.Temperature_icon_holder_shadow.setObjectName(u"Temperature_icon_holder_shadow")
        self.Temperature_icon_holder_shadow.setEnabled(False)
        self.Temperature_icon_holder_shadow.setGeometry(QRect(30, 36, 141, 131))
        self.Temperature_icon_holder_shadow.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:rgba(0,0,0,0.1);\n"
"border-radius:40%;\n"
"}")
        self.Temperature_icon_holder_shadow.setFrameShape(QFrame.NoFrame)
        self.Temperature_icon_holder_shadow.setFrameShadow(QFrame.Raised)
        self.Temperatur_icon = QFrame(self.Temperature_holder)
        self.Temperatur_icon.setObjectName(u"Temperatur_icon")
        self.Temperatur_icon.setEnabled(False)
        self.Temperatur_icon.setGeometry(QRect(30, 30, 141, 131))
        self.Temperatur_icon.setStyleSheet(u"QFrame\n"
"\n"
"{\n"
"	\n"
"\n"
"	background-color: hsv(212, 111, 90);\n"
"\n"
"border-radius:40%;\n"
"}")
        self.Temperatur_icon.setFrameShape(QFrame.NoFrame)
        self.Temperatur_icon.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.Temperatur_icon)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(14, 23, 120, 80))
        self.frame_2.setStyleSheet(u"image: url(:/prefix/icons/thermometer.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.Celsius_2 = QLabel(self.Temperature_holder)
        self.Celsius_2.setObjectName(u"Celsius_2")
        self.Celsius_2.setGeometry(QRect(290, 100, 31, 41))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.Celsius_2.setPalette(palette2)
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(False)
        font5.setWeight(50)
        self.Celsius_2.setFont(font5)
        self.Celsius_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(255,255,255);")
        self.Celsius_label = QLabel(self.Temperature_holder)
        self.Celsius_label.setObjectName(u"Celsius_label")
        self.Celsius_label.setGeometry(QRect(300, 100, 51, 61))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.Celsius_label.setPalette(palette3)
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setWeight(50)
        self.Celsius_label.setFont(font6)
        self.Celsius_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(255,255,255);")
        self.frame_3 = QFrame(self.Temperature_holder)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(430, 20, 71, 151))
        self.frame_3.setStyleSheet(u"border-radius:30%;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(3, 62, 61, 71))
        self.frame_14.setStyleSheet(u"background-color:None;\n"
"image: url(:/prefix/icons/equalizer.png);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(2, 16, 61, 71))
        self.frame_15.setStyleSheet(u"background-color:None;\n"
"image: url(:/prefix/icons/equalizer.png);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.Temperature_icon_holder_shadow.raise_()
        self.Temperatur_icon.raise_()
        self.Temperature.raise_()
        self.Temperature_label.raise_()
        self.Celsius_2.raise_()
        self.Celsius_label.raise_()
        self.frame_3.raise_()
        self.Humidity_holder = QFrame(self.frame)
        self.Humidity_holder.setObjectName(u"Humidity_holder")
        self.Humidity_holder.setGeometry(QRect(610, 380, 521, 191))
        self.Humidity_holder.setAutoFillBackground(False)
        self.Humidity_holder.setStyleSheet(u"\n"
"\n"
"\n"
"background-color: rgba(136, 190, 240,0.14);\n"
"\n"
"\n"
"\n"
"border-radius: 50%;\n"
"")
        self.Humidity_holder.setFrameShape(QFrame.StyledPanel)
        self.Humidity_holder.setFrameShadow(QFrame.Raised)
        self.Humidity_holder.setLineWidth(3)
        self.Humidity_holder.setMidLineWidth(3)
        self.Humidity = QLabel(self.Humidity_holder)
        self.Humidity.setObjectName(u"Humidity")
        self.Humidity.setGeometry(QRect(180, 80, 131, 91))
        self.Humidity.setFont(font4)
        self.Humidity.setStyleSheet(u"color: #ffffff;\n"
"background-color:None;\n"
"")
        self.Humidity.setAlignment(Qt.AlignCenter)
        self.Humdity_label = QLineEdit(self.Humidity_holder)
        self.Humdity_label.setObjectName(u"Humdity_label")
        self.Humdity_label.setGeometry(QRect(180, 20, 201, 51))
        self.Humdity_label.setFont(font3)
        self.Humdity_label.setStyleSheet(u"color: white;\n"
"font-size: 30px;\n"
"background-color: rgba(0,0,0,0);")
        self.Humdity_label.setAlignment(Qt.AlignCenter)
        self.Humdity_icon_holder_shadow_2 = QFrame(self.Humidity_holder)
        self.Humdity_icon_holder_shadow_2.setObjectName(u"Humdity_icon_holder_shadow_2")
        self.Humdity_icon_holder_shadow_2.setEnabled(False)
        self.Humdity_icon_holder_shadow_2.setGeometry(QRect(30, 36, 141, 131))
        self.Humdity_icon_holder_shadow_2.setStyleSheet(u"QFrame\n"
"{\n"
"\n"
"	background-color:rgba(0,0,0,0.1);\n"
"border-radius:40%;\n"
"}")
        self.Humdity_icon_holder_shadow_2.setFrameShape(QFrame.NoFrame)
        self.Humdity_icon_holder_shadow_2.setFrameShadow(QFrame.Raised)
        self.Humidity_icon = QFrame(self.Humidity_holder)
        self.Humidity_icon.setObjectName(u"Humidity_icon")
        self.Humidity_icon.setEnabled(False)
        self.Humidity_icon.setGeometry(QRect(30, 30, 141, 131))
        self.Humidity_icon.setStyleSheet(u"QFrame\n"
"\n"
"{\n"
"	\n"
"\n"
"	background-color: hsv(212, 111, 90);\n"
"\n"
"border-radius:40%;\n"
"}")
        self.Humidity_icon.setFrameShape(QFrame.NoFrame)
        self.Humidity_icon.setFrameShadow(QFrame.Raised)
        self.Humdity_icon_holder = QFrame(self.Humidity_icon)
        self.Humdity_icon_holder.setObjectName(u"Humdity_icon_holder")
        self.Humdity_icon_holder.setGeometry(QRect(10, 23, 120, 80))
        self.Humdity_icon_holder.setStyleSheet(u"image: url(:/prefix/icons/humidity.png);")
        self.Humdity_icon_holder.setFrameShape(QFrame.StyledPanel)
        self.Humdity_icon_holder.setFrameShadow(QFrame.Raised)
        self.Percentage_label = QLabel(self.Humidity_holder)
        self.Percentage_label.setObjectName(u"Percentage_label")
        self.Percentage_label.setGeometry(QRect(290, 100, 51, 61))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush14)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush15 = QBrush(QColor(255, 255, 255, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush16 = QBrush(QColor(255, 255, 255, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.Percentage_label.setPalette(palette4)
        self.Percentage_label.setFont(font6)
        self.Percentage_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(255,255,255);")
        self.frame_17 = QFrame(self.Humidity_holder)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(430, 20, 71, 151))
        self.frame_17.setStyleSheet(u"border-radius:30%;\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(16, 10, 41, 31))
        self.frame_16.setStyleSheet(u"background-color:None;\n"
"image: url(:/prefix/icons/upward_arrow.png);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(16, 110, 41, 31))
        self.frame_18.setStyleSheet(u"background-color:None;\n"
"image: url(:/prefix/icons/downward_arrow.png);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.Chart = QFrame(self.frame)
        self.Chart.setObjectName(u"Chart")
        self.Chart.setGeometry(QRect(50, 630, 1081, 271))
        self.Chart.setStyleSheet(u"\n"
"background-color: rgb(39, 53, 69);\n"
"")
        self.Chart.setFrameShape(QFrame.StyledPanel)
        self.Chart.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.Chart)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 20, 121, 16))
        font7 = QFont()
        font7.setPointSize(13)
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"color:White;\n"
"background-color:None;")
        self.Gate_control = QFrame(self.frame)
        self.Gate_control.setObjectName(u"Gate_control")
        self.Gate_control.setGeometry(QRect(1170, 630, 291, 271))
        self.Gate_control.setStyleSheet(u"background-color: rgb(41, 55, 74);")
        self.Gate_control.setFrameShape(QFrame.StyledPanel)
        self.Gate_control.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.Gate_control)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 200, 91, 51))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush17 = QBrush(QColor(22, 27, 34, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush17)
        brush18 = QBrush(QColor(255, 255, 255, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        brush19 = QBrush(QColor(255, 255, 255, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        brush20 = QBrush(QColor(255, 255, 255, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.pushButton.setPalette(palette5)
        font8 = QFont()
        font8.setFamily(u"Rockwell")
        font8.setPointSize(15)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(22, 27, 34);\n"
"\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(193, 197, 194);\n"
"\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 148, 0);\n"
"border: 2px solid rgb(114, 4, 231);\n"
"	\n"
"}")
        self.verticalSlider = QSlider(self.Gate_control)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(210, 20, 41, 171))
        self.verticalSlider.setStyleSheet(u"QSlider::groove {\n"
"    border:2px solid #30363D;\n"
"    width: 5px;\n"
"	background-color: rgb(67, 82, 104);\n"
" \n"
"    margin: 0 16px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background:rgba(0,0,0);\n"
"    border: 2px solid #C9CEC9;\n"
"    height: 20px;\n"
"    margin: 0px -15px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:hover {\n"
"    background: rgba(255, 148, 0);\n"
"    border: 2px solid rgba(114, 4, 231);\n"
"    height: 20px;\n"
"    margin: 0px -15px;\n"
"	border-radius: 7px;\n"
"}")
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.frame_8 = QFrame(self.Gate_control)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(30, 60, 141, 131))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(19, 9, 111, 111))
        self.frame_19.setStyleSheet(u"border-radius: 55px;\n"
"	\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(229, 132, 0, 255));\n"
"")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(10, 10, 91, 91))
        self.frame_20.setStyleSheet(u"border-radius: 45px;\n"
"background-color: rgb(22, 29, 39);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_20)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 22, 51, 41))
        font9 = QFont()
        font9.setPointSize(20)
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(68, 11, 16, 16))
        self.label_2.setStyleSheet(u"color:white;\n"
"background-color:None;")
        self.label_3 = QLabel(self.Gate_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(19, 20, 121, 21))
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.Server_details = QFrame(self.frame)
        self.Server_details.setObjectName(u"Server_details")
        self.Server_details.setGeometry(QRect(1170, 380, 291, 191))
        self.Server_details.setStyleSheet(u"background-color: rgb(41, 55, 74);")
        self.Server_details.setFrameShape(QFrame.StyledPanel)
        self.Server_details.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.Server_details)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(220, 80, 291, 191))
        self.frame_9.setStyleSheet(u"background-color: rgb(41, 55, 74);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.Server_details)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(19, 20, 141, 21))
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.label_5 = QLabel(self.Server_details)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 70, 91, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.IP_address = QLabel(self.Server_details)
        self.IP_address.setObjectName(u"IP_address")
        self.IP_address.setGeometry(QRect(120, 70, 91, 21))
        font10 = QFont()
        font10.setPointSize(9)
        self.IP_address.setFont(font10)
        self.IP_address.setStyleSheet(u"Background-color: None;\n"
"color:White;\n"
"")
        self.label_6 = QLabel(self.Server_details)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 110, 41, 21))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.Port = QLabel(self.Server_details)
        self.Port.setObjectName(u"Port")
        self.Port.setGeometry(QRect(70, 110, 91, 21))
        self.Port.setFont(font10)
        self.Port.setStyleSheet(u"Background-color: None;\n"
"color:White;\n"
"")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1170, 80, 291, 251))
        self.frame_7.setStyleSheet(u"background-color: rgb(41, 55, 74);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 41, 21))
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 70, 61, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 110, 71, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"Background-color:None;\n"
"color:white;")
        self.SOS_btn = QPushButton(self.frame_7)
        self.SOS_btn.setObjectName(u"SOS_btn")
        self.SOS_btn.setGeometry(QRect(100, 160, 81, 71))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush17)
        brush21 = QBrush(QColor(255, 255, 255, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush21)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        brush22 = QBrush(QColor(255, 255, 255, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        brush23 = QBrush(QColor(255, 255, 255, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.SOS_btn.setPalette(palette6)
        self.SOS_btn.setFont(font8)
        self.SOS_btn.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"background-color: rgb(22, 27, 34);\n"
"\n"
"border-radius: 25px;\n"
"border: 2px solid  rgb(193, 197, 194);\n"
"\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 148, 0);\n"
"border: 2px solid rgb(114, 4, 231);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/prefix/icons/sos icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SOS_btn.setIcon(icon)
        self.SOS_btn.setIconSize(QSize(35, 35))
        self.Emergency_name = QLabel(self.frame_7)
        self.Emergency_name.setObjectName(u"Emergency_name")
        self.Emergency_name.setGeometry(QRect(80, 70, 91, 21))
        self.Emergency_name.setFont(font10)
        self.Emergency_name.setStyleSheet(u"Background-color: None;\n"
"color:White;\n"
"")
        self.Emergency_name_2 = QLabel(self.frame_7)
        self.Emergency_name_2.setObjectName(u"Emergency_name_2")
        self.Emergency_name_2.setGeometry(QRect(90, 110, 91, 21))
        self.Emergency_name_2.setFont(font10)
        self.Emergency_name_2.setStyleSheet(u"Background-color: None;\n"
"color:White;\n"
"")
        self.SMS_signal = QFrame(self.frame_7)
        self.SMS_signal.setObjectName(u"SMS_signal")
        self.SMS_signal.setGeometry(QRect(189, 20, 81, 51))
        self.SMS_signal.setStyleSheet(u"background-color: rgb(26, 34, 47);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.SMS_signal.setFrameShape(QFrame.StyledPanel)
        self.SMS_signal.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.SMS_signal)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 11, 61, 31))
        self.frame_10.setStyleSheet(u"image: url(:/prefix/icons/sms.png);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 680, 1041, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Waterlevel_holder_shadow.raise_()
        self.Waterlevel_holder.raise_()
        self.WaterlevelBG.raise_()
        self.Flowrate_holder_shadow.raise_()
        self.Flowrate_holder.raise_()
        self.Close.raise_()
        self.Minimize.raise_()
        self.frame_5.raise_()
        self.FlowrateBG.raise_()
        self.Temperature_holder.raise_()
        self.Humidity_holder.raise_()
        self.Chart.raise_()
        self.Gate_control.raise_()
        self.Server_details.raise_()
        self.frame_7.raise_()
        self.gridLayoutWidget.raise_()
        Dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"MainWindow", None))
        self.Close.setText("")
        self.Minimize.setText("")
        self.Flowrate.setText(QCoreApplication.translate("Dashboard", u"0", None))
        self.LPM.setText(QCoreApplication.translate("Dashboard", u"LPM", None))
        self.Flowrate_label.setText(QCoreApplication.translate("Dashboard", u"Flow rate", None))
        self.Waterlevel.setText(QCoreApplication.translate("Dashboard", u"0", None))
        self.cm.setText(QCoreApplication.translate("Dashboard", u"cm", None))
        self.Waterlevel_label_2.setText(QCoreApplication.translate("Dashboard", u"Water level", None))
        self.Temperature.setText(QCoreApplication.translate("Dashboard", u"0", None))
        self.Temperature_label.setText(QCoreApplication.translate("Dashboard", u"Temperature", None))
        self.Celsius_2.setText(QCoreApplication.translate("Dashboard", u"\u00b0", None))
        self.Celsius_label.setText(QCoreApplication.translate("Dashboard", u"C", None))
        self.Humidity.setText(QCoreApplication.translate("Dashboard", u"0", None))
        self.Humdity_label.setText(QCoreApplication.translate("Dashboard", u"Humidity", None))
        self.Percentage_label.setText(QCoreApplication.translate("Dashboard", u"%", None))
        self.label_10.setText(QCoreApplication.translate("Dashboard", u"Water Level", None))
        self.pushButton.setText(QCoreApplication.translate("Dashboard", u"Rotate", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Dashboard", u"o", None))
        self.label_3.setText(QCoreApplication.translate("Dashboard", u"Gate Control", None))
        self.label_4.setText(QCoreApplication.translate("Dashboard", u"Server details", None))
        self.label_5.setText(QCoreApplication.translate("Dashboard", u"IP Address:", None))
        self.IP_address.setText(QCoreApplication.translate("Dashboard", u"192.168.1.1", None))
        self.label_6.setText(QCoreApplication.translate("Dashboard", u"Port:", None))
        self.Port.setText(QCoreApplication.translate("Dashboard", u"5050", None))
        self.label_7.setText(QCoreApplication.translate("Dashboard", u"SOS", None))
        self.label_8.setText(QCoreApplication.translate("Dashboard", u"Name:", None))
        self.label_9.setText(QCoreApplication.translate("Dashboard", u"Number:", None))
        self.SOS_btn.setText("")
        self.Emergency_name.setText(QCoreApplication.translate("Dashboard", u"Danish", None))
        self.Emergency_name_2.setText(QCoreApplication.translate("Dashboard", u"854614750", None))
    # retranslateUi

