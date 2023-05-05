# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHRMcwK.ui'
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

from icons import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1173, 657)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #ececec;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy1)
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(250, 16777215))
        self.slide_menu_container.setStyleSheet(u"background-color: rgb(35,37,50);")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        font = QFont()
        font.setPointSize(7)
        self.slide_menu.setFont(font)
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo_container = QFrame(self.slide_menu)
        self.logo_container.setObjectName(u"logo_container")
        self.logo_container.setFrameShape(QFrame.StyledPanel)
        self.logo_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.logo_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 4, -1, -1)
        self.logo = QLabel(self.logo_container)
        self.logo.setObjectName(u"logo")
        font1 = QFont()
        font1.setFamily(u"Impact")
        font1.setPointSize(14)
        font1.setUnderline(False)
        self.logo.setFont(font1)
        self.logo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.logo, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.logo_container)

        self.menu_container = QFrame(self.slide_menu)
        self.menu_container.setObjectName(u"menu_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_container.sizePolicy().hasHeightForWidth())
        self.menu_container.setSizePolicy(sizePolicy2)
        self.menu_container.setFrameShape(QFrame.StyledPanel)
        self.menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.menu_container)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.menu_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame)

        self.slide_menu_buttons_container = QFrame(self.menu_container)
        self.slide_menu_buttons_container.setObjectName(u"slide_menu_buttons_container")
        self.slide_menu_buttons_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_buttons_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.slide_menu_buttons_container)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scraper_button_container = QFrame(self.slide_menu_buttons_container)
        self.scraper_button_container.setObjectName(u"scraper_button_container")
        sizePolicy.setHeightForWidth(self.scraper_button_container.sizePolicy().hasHeightForWidth())
        self.scraper_button_container.setSizePolicy(sizePolicy)
        self.scraper_button_container.setStyleSheet(u"")
        self.scraper_button_container.setFrameShape(QFrame.StyledPanel)
        self.scraper_button_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.scraper_button_container)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 30, 0)
        self.scraper_button = QPushButton(self.scraper_button_container)
        self.scraper_button.setObjectName(u"scraper_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scraper_button.sizePolicy().hasHeightForWidth())
        self.scraper_button.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.scraper_button.setFont(font2)
        self.scraper_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.scraper_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-funnel-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scraper_button.setIcon(icon)
        self.scraper_button.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.scraper_button)


        self.verticalLayout_9.addWidget(self.scraper_button_container)

        self.sender_button_container = QFrame(self.slide_menu_buttons_container)
        self.sender_button_container.setObjectName(u"sender_button_container")
        self.sender_button_container.setFrameShape(QFrame.StyledPanel)
        self.sender_button_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.sender_button_container)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 30, 0)
        self.sender_button = QPushButton(self.sender_button_container)
        self.sender_button.setObjectName(u"sender_button")
        self.sender_button.setFont(font2)
        self.sender_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.sender_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-send-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sender_button.setIcon(icon1)
        self.sender_button.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.sender_button)


        self.verticalLayout_9.addWidget(self.sender_button_container)

        self.frame_7 = QFrame(self.slide_menu_buttons_container)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.slide_menu_buttons_container)

        self.frame_4 = QFrame(self.menu_container)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.menu_container)

        self.settings_button_container = QFrame(self.slide_menu)
        self.settings_button_container.setObjectName(u"settings_button_container")
        sizePolicy.setHeightForWidth(self.settings_button_container.sizePolicy().hasHeightForWidth())
        self.settings_button_container.setSizePolicy(sizePolicy)
        self.settings_button_container.setStyleSheet(u"background-color: rgb(25,26,36);")
        self.settings_button_container.setFrameShape(QFrame.StyledPanel)
        self.settings_button_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.settings_button_container)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 12, -1, 12)
        self.settings_button = QPushButton(self.settings_button_container)
        self.settings_button.setObjectName(u"settings_button")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift SemiBold")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.settings_button.setFont(font3)
        self.settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-settings-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon2)
        self.settings_button.setFlat(True)

        self.verticalLayout_5.addWidget(self.settings_button)


        self.verticalLayout_3.addWidget(self.settings_button_container)


        self.verticalLayout_7.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body1 = QFrame(self.centralwidget)
        self.main_body1.setObjectName(u"main_body1")
        sizePolicy.setHeightForWidth(self.main_body1.sizePolicy().hasHeightForWidth())
        self.main_body1.setSizePolicy(sizePolicy)
        self.main_body1.setFrameShape(QFrame.StyledPanel)
        self.main_body1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body1)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(42,45,60);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_button_container = QFrame(self.header_frame)
        self.menu_button_container.setObjectName(u"menu_button_container")
        self.menu_button_container.setFrameShape(QFrame.StyledPanel)
        self.menu_button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.menu_button_container)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 15, -1, 15)
        self.menu_button = QPushButton(self.menu_button_container)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-menu-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon3)
        self.menu_button.setIconSize(QSize(32, 32))
        self.menu_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.menu_button, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_button_container)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.window_options_container = QFrame(self.header_frame)
        self.window_options_container.setObjectName(u"window_options_container")
        self.window_options_container.setFrameShape(QFrame.StyledPanel)
        self.window_options_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.window_options_container)
        self.horizontalLayout_5.setSpacing(18)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 15, -1, 15)
        self.minimize_button = QPushButton(self.window_options_container)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy5)
        self.minimize_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-horizontal-line-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon4)
        self.minimize_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.minimize_button)

        self.x_button = QPushButton(self.window_options_container)
        self.x_button.setObjectName(u"x_button")
        sizePolicy5.setHeightForWidth(self.x_button.sizePolicy().hasHeightForWidth())
        self.x_button.setSizePolicy(sizePolicy5)
        self.x_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons8-close-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.x_button.setIcon(icon5)
        self.x_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.x_button)


        self.horizontalLayout_3.addWidget(self.window_options_container, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body1_content = QFrame(self.main_body1)
        self.main_body1_content.setObjectName(u"main_body1_content")
        sizePolicy2.setHeightForWidth(self.main_body1_content.sizePolicy().hasHeightForWidth())
        self.main_body1_content.setSizePolicy(sizePolicy2)
        self.main_body1_content.setFrameShape(QFrame.StyledPanel)
        self.main_body1_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body1_content)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body1_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.scraper_page = QWidget()
        self.scraper_page.setObjectName(u"scraper_page")
        self.verticalLayout_8 = QVBoxLayout(self.scraper_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scraper_label = QLabel(self.scraper_page)
        self.scraper_label.setObjectName(u"scraper_label")
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiBold")
        font4.setPointSize(35)
        font4.setBold(True)
        font4.setWeight(75)
        self.scraper_label.setFont(font4)
        self.scraper_label.setStyleSheet(u"color: rgb(170, 170, 255);")

        self.verticalLayout_8.addWidget(self.scraper_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.scraper_page)
        self.sender_page = QWidget()
        self.sender_page.setObjectName(u"sender_page")
        self.verticalLayout_16 = QVBoxLayout(self.sender_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sender_label = QLabel(self.sender_page)
        self.sender_label.setObjectName(u"sender_label")
        self.sender_label.setFont(font4)
        self.sender_label.setStyleSheet(u"color: rgb(170, 170, 255);")

        self.verticalLayout_16.addWidget(self.sender_label, 0, Qt.AlignTop)

        self.settings_container_2 = QFrame(self.sender_page)
        self.settings_container_2.setObjectName(u"settings_container_2")
        sizePolicy2.setHeightForWidth(self.settings_container_2.sizePolicy().hasHeightForWidth())
        self.settings_container_2.setSizePolicy(sizePolicy2)
        self.settings_container_2.setFrameShape(QFrame.StyledPanel)
        self.settings_container_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.settings_container_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.enteremail_label = QLabel(self.settings_container_2)
        self.enteremail_label.setObjectName(u"enteremail_label")
        font5 = QFont()
        font5.setFamily(u"Bahnschrift SemiBold")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.enteremail_label.setFont(font5)

        self.verticalLayout_17.addWidget(self.enteremail_label, 0, Qt.AlignBottom)

        self.emaillist_container = QFrame(self.settings_container_2)
        self.emaillist_container.setObjectName(u"emaillist_container")
        self.emaillist_container.setFrameShape(QFrame.StyledPanel)
        self.emaillist_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.emaillist_container)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.emaillist_input = QPlainTextEdit(self.emaillist_container)
        self.emaillist_input.setObjectName(u"emaillist_input")
        sizePolicy.setHeightForWidth(self.emaillist_input.sizePolicy().hasHeightForWidth())
        self.emaillist_input.setSizePolicy(sizePolicy)
        self.emaillist_input.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"border-bottom: 3px solid rgb(190, 184, 255);\n"
"margin-left: 10px;\n"
"margin-top: 10px;\n"
"margin-right: 10px;\n"
"padding: 10px;")

        self.horizontalLayout_13.addWidget(self.emaillist_input)


        self.verticalLayout_17.addWidget(self.emaillist_container)

        self.sendingemail_container = QFrame(self.settings_container_2)
        self.sendingemail_container.setObjectName(u"sendingemail_container")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sendingemail_container.sizePolicy().hasHeightForWidth())
        self.sendingemail_container.setSizePolicy(sizePolicy6)
        self.sendingemail_container.setFrameShape(QFrame.StyledPanel)
        self.sendingemail_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.sendingemail_container)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.sending_label = QLabel(self.sendingemail_container)
        self.sending_label.setObjectName(u"sending_label")
        sizePolicy6.setHeightForWidth(self.sending_label.sizePolicy().hasHeightForWidth())
        self.sending_label.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.sending_label, 0, Qt.AlignRight)

        self.sendingemail_label = QLabel(self.sendingemail_container)
        self.sendingemail_label.setObjectName(u"sendingemail_label")
        sizePolicy6.setHeightForWidth(self.sendingemail_label.sizePolicy().hasHeightForWidth())
        self.sendingemail_label.setSizePolicy(sizePolicy6)
        self.sendingemail_label.setStyleSheet(u"color: rgb(85, 85, 255);")

        self.horizontalLayout_14.addWidget(self.sendingemail_label, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.sendingemail_container)

        self.sendbutton_container = QFrame(self.settings_container_2)
        self.sendbutton_container.setObjectName(u"sendbutton_container")
        font6 = QFont()
        font6.setPointSize(10)
        self.sendbutton_container.setFont(font6)
        self.sendbutton_container.setFrameShape(QFrame.StyledPanel)
        self.sendbutton_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.sendbutton_container)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.send_button = QPushButton(self.sendbutton_container)
        self.send_button.setObjectName(u"send_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy7)
        self.send_button.setMinimumSize(QSize(80, 0))
        font7 = QFont()
        font7.setFamily(u"Bahnschrift SemiBold")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.send_button.setFont(font7)
        self.send_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.send_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 170, 255);\n"
"    border: 2px solid rgb(170, 170, 255);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgb(21, 255, 189);\n"
"    border: 2px solid rgb(21, 255, 189);\n"
"}")

        self.horizontalLayout_8.addWidget(self.send_button)


        self.verticalLayout_17.addWidget(self.sendbutton_container, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.settings_container_2)

        self.stackedWidget.addWidget(self.sender_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"background-color: rgb(51, 46, 88);\n"
"background-color: #484177;")
        self.verticalLayout_12 = QVBoxLayout(self.settings_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.settings_label = QLabel(self.settings_page)
        self.settings_label.setObjectName(u"settings_label")
        sizePolicy6.setHeightForWidth(self.settings_label.sizePolicy().hasHeightForWidth())
        self.settings_label.setSizePolicy(sizePolicy6)
        self.settings_label.setFont(font4)
        self.settings_label.setStyleSheet(u"color: rgb(243, 235, 255);")

        self.verticalLayout_12.addWidget(self.settings_label)

        self.settings_warning_frame = QFrame(self.settings_page)
        self.settings_warning_frame.setObjectName(u"settings_warning_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.settings_warning_frame.sizePolicy().hasHeightForWidth())
        self.settings_warning_frame.setSizePolicy(sizePolicy8)
        self.settings_warning_frame.setMinimumSize(QSize(0, 0))
        self.settings_warning_frame.setStyleSheet(u"")
        self.settings_warning_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_warning_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.settings_warning_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.settings_warning_label = QLabel(self.settings_warning_frame)
        self.settings_warning_label.setObjectName(u"settings_warning_label")

        self.verticalLayout_14.addWidget(self.settings_warning_label)


        self.verticalLayout_12.addWidget(self.settings_warning_frame, 0, Qt.AlignHCenter)

        self.settings_container = QFrame(self.settings_page)
        self.settings_container.setObjectName(u"settings_container")
        self.settings_container.setFrameShape(QFrame.StyledPanel)
        self.settings_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.settings_container)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.email_container = QFrame(self.settings_container)
        self.email_container.setObjectName(u"email_container")
        self.email_container.setFrameShape(QFrame.StyledPanel)
        self.email_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.email_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.email_label = QLabel(self.email_container)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font7)
        self.email_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.email_label, 0, Qt.AlignRight)

        self.email_input = QLineEdit(self.email_container)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(250, 0))
        self.email_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	padding: 8px;\n"
"	border-radius: 15px;\n"
"	border-bottom: 3px solid #3B324E;\n"
"	font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 80, 247);\n"
"}")

        self.horizontalLayout_2.addWidget(self.email_input, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.email_container, 0, Qt.AlignHCenter)

        self.password_container = QFrame(self.settings_container)
        self.password_container.setObjectName(u"password_container")
        self.password_container.setFrameShape(QFrame.StyledPanel)
        self.password_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.password_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.password_label = QLabel(self.password_container)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font7)
        self.password_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.password_label, 0, Qt.AlignRight)

        self.password_input = QLineEdit(self.password_container)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(250, 0))
        self.password_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	padding: 8px;\n"
"	border-radius: 15px;\n"
"	border-bottom: 3px solid #3B324E;\n"
"	font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 80, 247);\n"
"}")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.password_input)


        self.verticalLayout_13.addWidget(self.password_container, 0, Qt.AlignHCenter)

        self.timeinterval_lcontainer = QFrame(self.settings_container)
        self.timeinterval_lcontainer.setObjectName(u"timeinterval_lcontainer")
        self.timeinterval_lcontainer.setFrameShape(QFrame.StyledPanel)
        self.timeinterval_lcontainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.timeinterval_lcontainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.timeinterval_label = QLabel(self.timeinterval_lcontainer)
        self.timeinterval_label.setObjectName(u"timeinterval_label")
        self.timeinterval_label.setFont(font7)
        self.timeinterval_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.timeinterval_label, 0, Qt.AlignRight)

        self.timeinterval_spinbox = QSpinBox(self.timeinterval_lcontainer)
        self.timeinterval_spinbox.setObjectName(u"timeinterval_spinbox")
        self.timeinterval_spinbox.setStyleSheet(u"QSpinBox {\n"
"	background-color: #fff;\n"
"	padding: 8px;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom: 3px solid #3B324E;\n"
"	font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"QSpinBox:focus {\n"
"	border: 3px solid rgb(255, 80, 247);\n"
"}")
        self.timeinterval_spinbox.setMaximum(999999999)

        self.horizontalLayout_12.addWidget(self.timeinterval_spinbox, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.timeinterval_lcontainer)

        self.subject_container = QFrame(self.settings_container)
        self.subject_container.setObjectName(u"subject_container")
        self.subject_container.setFrameShape(QFrame.StyledPanel)
        self.subject_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.subject_container)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.subject_label = QLabel(self.subject_container)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setFont(font7)
        self.subject_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.subject_label)

        self.subject_input = QLineEdit(self.subject_container)
        self.subject_input.setObjectName(u"subject_input")
        self.subject_input.setMinimumSize(QSize(250, 0))
        self.subject_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: #fff;\n"
"	padding: 8px;\n"
"	border-radius: 15px;\n"
"	border-bottom: 3px solid #3B324E;\n"
"	font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 80, 247);\n"
"}")

        self.horizontalLayout_10.addWidget(self.subject_input)


        self.verticalLayout_13.addWidget(self.subject_container)

        self.content_frame = QFrame(self.settings_container)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.content_label = QLabel(self.content_frame)
        self.content_label.setObjectName(u"content_label")
        self.content_label.setFont(font7)
        self.content_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.content_label)

        self.content_input = QTextEdit(self.content_frame)
        self.content_input.setObjectName(u"content_input")
        self.content_input.setStyleSheet(u"QTextEdit {\n"
"	background-color: #fff;\n"
"	padding: 8px;\n"
"	border-radius: 15px;\n"
"	border-bottom: 3px solid #3B324E;\n"
"	font: 25 9pt \"Bahnschrift Light\";\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 3px solid rgb(255, 80, 247);\n"
"}")

        self.horizontalLayout_11.addWidget(self.content_input)


        self.verticalLayout_13.addWidget(self.content_frame)

        self.save_container = QFrame(self.settings_container)
        self.save_container.setObjectName(u"save_container")
        self.save_container.setMinimumSize(QSize(0, 0))
        self.save_container.setFrameShape(QFrame.StyledPanel)
        self.save_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.save_container)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.save_button = QPushButton(self.save_container)
        self.save_button.setObjectName(u"save_button")
        sizePolicy5.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy5)
        font8 = QFont()
        font8.setPointSize(8)
        self.save_button.setFont(font8)
        self.save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_button.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(16, 255, 164);\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}\n"
"QPushButton:Hover{\n"
"	border: 2px solid #fff;\n"
"	background-color: rgb(31, 229, 147);\n"
"}")

        self.verticalLayout_15.addWidget(self.save_button, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.save_container)


        self.verticalLayout_12.addWidget(self.settings_container)

        self.stackedWidget.addWidget(self.settings_page)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body1_content)

        self.footer = QFrame(self.main_body1)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.version_container = QFrame(self.footer)
        self.version_container.setObjectName(u"version_container")
        self.version_container.setFrameShape(QFrame.StyledPanel)
        self.version_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.version_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.version = QLabel(self.version_container)
        self.version.setObjectName(u"version")
        font9 = QFont()
        font9.setFamily(u"Impact")
        font9.setPointSize(11)
        self.version.setFont(font9)
        self.version.setStyleSheet(u"color: rgb(170, 170, 255);")

        self.verticalLayout_2.addWidget(self.version, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.version_container)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"EMAIL SCRAPER", None))
        self.scraper_button.setText(QCoreApplication.translate("MainWindow", u"Scraper", None))
        self.sender_button.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menu_button.setText("")
        self.minimize_button.setText("")
        self.x_button.setText("")
        self.scraper_label.setText(QCoreApplication.translate("MainWindow", u"Scraper", None))
        self.sender_label.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.enteremail_label.setText(QCoreApplication.translate("MainWindow", u"Enter a list of emails. Each email goes on a new line.", None))
        self.emaillist_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter emails here...", None))
        self.sending_label.setText("")
        self.sendingemail_label.setText("")
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settings_warning_label.setText("")
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"Sender Email:    ", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Email Password:", None))
        self.timeinterval_label.setText(QCoreApplication.translate("MainWindow", u"Time Interval Between Sending Emails (seconds):", None))
        self.subject_label.setText(QCoreApplication.translate("MainWindow", u"Email Subject: ", None))
        self.content_label.setText(QCoreApplication.translate("MainWindow", u"Email Content:", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

