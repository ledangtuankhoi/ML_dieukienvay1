# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_base_old.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy2)
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.btn_open_file = QPushButton(self.frame_menus)
        self.btn_open_file.setObjectName(u"btn_open_file")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_open_file.sizePolicy().hasHeightForWidth())
        self.btn_open_file.setSizePolicy(sizePolicy3)
        self.btn_open_file.setMinimumSize(QSize(0, 60))
        self.btn_open_file.setFont(font2)
        self.btn_open_file.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_file.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-folder-open.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	border-right: 5px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_open_file)

        self.btn_save = QPushButton(self.frame_menus)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy3.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy3)
        self.btn_save.setMinimumSize(QSize(0, 60))
        self.btn_save.setFont(font2)
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-save.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_save)

        self.btn_new = QPushButton(self.frame_menus)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy3.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy3)
        self.btn_new.setMinimumSize(QSize(0, 60))
        self.btn_new.setFont(font2)
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-file.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_new)

        self.btn_new_user = QPushButton(self.frame_menus)
        self.btn_new_user.setObjectName(u"btn_new_user")
        sizePolicy3.setHeightForWidth(self.btn_new_user.sizePolicy().hasHeightForWidth())
        self.btn_new_user.setSizePolicy(sizePolicy3)
        self.btn_new_user.setMinimumSize(QSize(0, 60))
        self.btn_new_user.setFont(font2)
        self.btn_new_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_user.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-user-follow.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_new_user)


        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy2.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy2)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)

        self.btn_settings = QPushButton(self.frame_extra_menus)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy3.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy3)
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font2)
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 26px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 26px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 26px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menu_bottom.addWidget(self.btn_settings)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stackedWidget.addWidget(self.page_home)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_9 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_3 = QLabel(self.page_settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_10.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_2 = QLabel(self.page_settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 6, 0, 1, 1)

        self.label_5 = QLabel(self.page_settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_10.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(self.page_settings)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.page_settings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(self.page_settings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 7, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_10)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.cob_lichsuvay = QComboBox(self.page_settings)
        self.cob_lichsuvay.addItem("")
        self.cob_lichsuvay.addItem("")
        self.cob_lichsuvay.addItem("")
        self.cob_lichsuvay.setObjectName(u"cob_lichsuvay")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.cob_lichsuvay.setFont(font5)
        self.cob_lichsuvay.setAutoFillBackground(False)
        self.cob_lichsuvay.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_lichsuvay.setIconSize(QSize(16, 16))
        self.cob_lichsuvay.setFrame(True)

        self.gridLayout_9.addWidget(self.cob_lichsuvay, 9, 0, 1, 1)

        self.txt_thunhap = QLineEdit(self.page_settings)
        self.txt_thunhap.setObjectName(u"txt_thunhap")
        self.txt_thunhap.setMinimumSize(QSize(0, 30))
        self.txt_thunhap.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_9.addWidget(self.txt_thunhap, 1, 0, 1, 1)

        self.txt_thunhapnguoithan = QLineEdit(self.page_settings)
        self.txt_thunhapnguoithan.setObjectName(u"txt_thunhapnguoithan")
        self.txt_thunhapnguoithan.setMinimumSize(QSize(0, 30))
        self.txt_thunhapnguoithan.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_9.addWidget(self.txt_thunhapnguoithan, 3, 0, 1, 1)

        self.txt_sotienvay = QLineEdit(self.page_settings)
        self.txt_sotienvay.setObjectName(u"txt_sotienvay")
        self.txt_sotienvay.setMinimumSize(QSize(0, 30))
        self.txt_sotienvay.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_9.addWidget(self.txt_sotienvay, 4, 0, 1, 1)

        self.txt_tgvay = QLineEdit(self.page_settings)
        self.txt_tgvay.setObjectName(u"txt_tgvay")
        self.txt_tgvay.setMinimumSize(QSize(0, 30))
        self.txt_tgvay.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_9.addWidget(self.txt_tgvay, 7, 0, 1, 1)

        self.txt_nguoiphuthuoc = QLineEdit(self.page_settings)
        self.txt_nguoiphuthuoc.setObjectName(u"txt_nguoiphuthuoc")
        self.txt_nguoiphuthuoc.setMinimumSize(QSize(0, 30))
        self.txt_nguoiphuthuoc.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_9.addWidget(self.txt_nguoiphuthuoc, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 10, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_9)


        self.gridLayout_6.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_6)

        self.label_8 = QLabel(self.page_settings)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_12 = QLabel(self.page_settings)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_11 = QLabel(self.page_settings)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_9 = QLabel(self.page_settings)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_10 = QLabel(self.page_settings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_7 = QLabel(self.page_settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 6, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_14)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_2, 8, 1, 1, 1)

        self.cob_honnhan = QComboBox(self.page_settings)
        self.cob_honnhan.setObjectName(u"cob_honnhan")
        self.cob_honnhan.setFont(font5)
        self.cob_honnhan.setAutoFillBackground(False)
        self.cob_honnhan.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_honnhan.setIconSize(QSize(16, 16))
        self.cob_honnhan.setFrame(True)

        self.gridLayout_12.addWidget(self.cob_honnhan, 2, 1, 1, 1)

        self.cob_hocvan = QComboBox(self.page_settings)
        self.cob_hocvan.setObjectName(u"cob_hocvan")
        self.cob_hocvan.setFont(font5)
        self.cob_hocvan.setAutoFillBackground(False)
        self.cob_hocvan.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_hocvan.setIconSize(QSize(16, 16))
        self.cob_hocvan.setFrame(True)

        self.gridLayout_12.addWidget(self.cob_hocvan, 3, 1, 1, 1)

        self.cob_tukinhdoanh = QComboBox(self.page_settings)
        self.cob_tukinhdoanh.setObjectName(u"cob_tukinhdoanh")
        self.cob_tukinhdoanh.setFont(font5)
        self.cob_tukinhdoanh.setAutoFillBackground(False)
        self.cob_tukinhdoanh.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_tukinhdoanh.setIconSize(QSize(16, 16))
        self.cob_tukinhdoanh.setFrame(True)

        self.gridLayout_12.addWidget(self.cob_tukinhdoanh, 4, 1, 1, 1)

        self.cob_gioitinh = QComboBox(self.page_settings)
        self.cob_gioitinh.setObjectName(u"cob_gioitinh")
        self.cob_gioitinh.setFont(font5)
        self.cob_gioitinh.setAutoFillBackground(False)
        self.cob_gioitinh.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_gioitinh.setIconSize(QSize(16, 16))
        self.cob_gioitinh.setFrame(True)

        self.gridLayout_12.addWidget(self.cob_gioitinh, 1, 1, 1, 1)

        self.cob_khuvuc = QComboBox(self.page_settings)
        self.cob_khuvuc.setObjectName(u"cob_khuvuc")
        self.cob_khuvuc.setFont(font5)
        self.cob_khuvuc.setAutoFillBackground(False)
        self.cob_khuvuc.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cob_khuvuc.setIconSize(QSize(16, 16))
        self.cob_khuvuc.setFrame(True)

        self.gridLayout_12.addWidget(self.cob_khuvuc, 6, 1, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_12)


        self.gridLayout_5.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)

        self.label_16 = QLabel(self.page_settings)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 2, 2, 1, 1)

        self.label_14 = QLabel(self.page_settings)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_13 = QLabel(self.page_settings)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.frame = QFrame(self.page_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.label_status = QLabel(self.frame_content_wid_1)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout_17.addWidget(self.label_status, 0, 0, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout_17)


        self.verticalLayout_8.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.gridLayout_2.addWidget(self.frame, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.page_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.frame_2)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_3 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.label_desi = QLabel(self.frame_content_wid_3)
        self.label_desi.setObjectName(u"label_desi")

        self.gridLayout_19.addWidget(self.label_desi, 0, 0, 1, 1)


        self.horizontalLayout_18.addLayout(self.gridLayout_19)


        self.verticalLayout_11.addWidget(self.frame_content_wid_3)


        self.verticalLayout_16.addWidget(self.frame_div_content_2)


        self.gridLayout_2.addWidget(self.frame_2, 1, 2, 1, 1)

        self.label_17 = QLabel(self.page_settings)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_submit = QPushButton(self.page_settings)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setMinimumSize(QSize(150, 30))
        self.btn_submit.setFont(font5)
        self.btn_submit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_submit.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_submit, 1, 0, 1, 1)

        self.btn_import = QPushButton(self.page_settings)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(150, 30))
        self.btn_import.setFont(font5)
        self.btn_import.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_import.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_import, 4, 0, 1, 1)

        self.btn_reset = QPushButton(self.page_settings)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(150, 30))
        self.btn_reset.setFont(font5)
        self.btn_reset.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_reset.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_reset, 2, 0, 1, 1)

        self.btn_export = QPushButton(self.page_settings)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setMinimumSize(QSize(150, 30))
        self.btn_export.setFont(font5)
        self.btn_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_export.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_export, 5, 0, 1, 1)

        self.label_15 = QLabel(self.page_settings)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.btn_about = QPushButton(self.page_settings)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(150, 30))
        self.btn_about.setFont(font5)
        self.btn_about.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_about.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_about, 3, 0, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_new_user.setText(QCoreApplication.translate("MainWindow", u"New User", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi H\u1ea1n Vay", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 Vay Tr\u01b0\u1edbc \u0110\u00e2y?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 Ti\u1ec1n Vay", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Thu Nh\u1eadp C\u1ee7a Ng\u01b0\u1eddi N\u1ed9p \u0110\u01a1n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 Ng\u01b0\u1eddi Ph\u1ee5 Thu\u1ed9c ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Thu Nh\u1eadp Ng\u01b0\u1eddi Th\u00e2n", None))
        self.cob_lichsuvay.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.cob_lichsuvay.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.cob_lichsuvay.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.txt_thunhap.setPlaceholderText(QCoreApplication.translate("MainWindow", u"x1000(VND)", None))
        self.txt_thunhapnguoithan.setPlaceholderText(QCoreApplication.translate("MainWindow", u"x1000(VND)", None))
        self.txt_sotienvay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"x1000(VND)", None))
        self.txt_tgvay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"x ng\u00e0y", None))
        self.txt_nguoiphuthuoc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"S\u1ed1 Ng\u01b0\u1eddi Ph\u1ee5 Thu\u1ed9c ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u".                                              .", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tr\u00ecnh \u0110\u1ed9 H\u1ecdc V\u1ea5n", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"T\u1ef1 Kinh Doanh", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Khu V\u1ef1c S\u1ed1ng", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"T\u00ecnh Tr\u1ea1ng H\u00f4n Nh\u00e2n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi T\u00ednh", None))
        self.label_16.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng S\u1ed1 Thu\u1eadt To\u00e1n", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft Qu\u1ea3", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_desi.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u".                                       .", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"X\u00e9t", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"L\u00e0m M\u1edbi", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Xu\u1ea5t", None))
        self.label_15.setText("")
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Chi Ti\u1ebft", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

