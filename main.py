import email
from email import contentmanager
from lib2to3.pytree import convert
import sys
from textwrap import indent
from turtle import width
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import ui_main
import json
import send_worker


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu Option
        # Remove Window Title Bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Set Main Background to Transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True) #100% transparent
        ##################
        ## Menu Buttons ##
        ##################
        # Close Window
        self.ui.x_button.clicked.connect(lambda: self.close())
        # Minimize Window
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        # Size Grip to Resize Window
        QSizeGrip(self.ui.size_grip)
        def moveWindow(e):
            # Detect if window is normal size
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow

        # Left Menu Toggle Button
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())

        # Show the Window
        self.show()

        ###########
        ## PAGES ##
        ###########        
        # Scraper PAGE
        self.ui.scraper_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.scraper_page))
        # Change button color when selected
        self.ui.scraper_button.clicked.connect(self.scraper_button_clicked)

        # Sender PAGE
        self.ui.sender_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sender_page))
        # Change button color when selected
        self.ui.sender_button.clicked.connect(self.sender_button_clicked)

        # Settings PAGE
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
        self.ui.settings_button.clicked.connect(self.settings_button_clicked)


        with open('config.json') as self.config:
            self.data = json.load(self.config)
        
        self.ui.email_input.setText(self.data["email"])
        self.ui.password_input.setText(self.data["password"])
        self.ui.timeinterval_spinbox.setValue(self.data["time_interval"])
        self.ui.subject_input.setText(self.data["subject"])
        self.ui.content_input.setText(self.data["content"])
        self.ui.emaillist_input.setPlainText(self.data["emails"])

        self.ui.email_input.textEdited.connect(lambda: self.email_edited())
        self.ui.password_input.textEdited.connect(lambda: self.password_edited())
        self.ui.timeinterval_spinbox.valueChanged.connect(lambda: self.timeinterval_edited())
        self.ui.subject_input.textEdited.connect(lambda: self.subject_edited())
        self.ui.content_input.textChanged.connect(lambda: self.content_edited())

        self.ui.save_button.clicked.connect(lambda: self.update_config(self.data))

        self.ui.send_button.clicked.connect(lambda: self.send_pressed(self.data))


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def slideLeftMenu(self):
        # Get cuttent width of left menu
        width = self.ui.slide_menu_container.width()

        # If closed
        if width == 0:
            newWidth = 250
        # If open
        else:
            newWidth = 0
        
        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250) # Animation takes 250ms to complete
        self.animation.setStartValue(width)  # Animation starts at where the menu is
        self.animation.setEndValue(newWidth) # Animation ends at the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart) # Set the animation type
        self.animation.start() # Start the animation

    def scraper_button_clicked(self):
        self.ui.sender_button.setStyleSheet(u'color: rgb(255, 255, 255);')
        self.ui.scraper_button.setStyleSheet(u"\
            color: rgb(255, 255, 255);\
            background-color: rgb(170, 170, 255);\
            border-radius: 15px;\
            padding: 4px;\
        ")

    def sender_button_clicked(self):
        self.ui.scraper_button.setStyleSheet(u'color: rgb(255, 255, 255);')
        self.ui.sender_button.setStyleSheet("\
            color: rgb(255, 255, 255);\
            background-color: rgb(170, 170, 255);\
            border-radius: 15px;\
            padding: 4px;\
        ")

    def settings_button_clicked(self):
        self.ui.sender_button.setStyleSheet(u'color: rgb(255, 255, 255);')
        self.ui.scraper_button.setStyleSheet(u'color: rgb(255, 255, 255);')

    def update_config(self, data, filename='config.json'):
        self.data["email"] = self.ui.email_input.text()
        self.data["password"] = self.ui.password_input.text()
        self.data["time_interval"] = self.ui.timeinterval_spinbox.value()
        self.data["subject"] = self.ui.subject_input.text()
        self.data["content"] = self.ui.content_input.toPlainText()
        self.email_edited()
        self.password_edited()
        self.timeinterval_edited()
        self.subject_edited()
        self.content_edited()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def email_edited(self):
        if self.ui.email_input.text() != self.data["email"]:
            self.ui.settings_warning_label.setText('WARNING! You have unsaved changes.')
            self.ui.settings_warning_label.setStyleSheet(u"color: rgb(255, 255, 255);\
            background-color: rgb(255, 152, 152);\
            border: 2px solid rgb(255, 98, 98);\
            border-radius: 8px;\
            padding: 6px;")
            self.ui.email_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border: 3px solid orange;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")
        else:
            self.ui.settings_warning_label.setText("")
            self.ui.settings_warning_label.setStyleSheet(u"")
            self.ui.email_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border-bottom: 3px solid #3B324E;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")

    def password_edited(self):
        if self.ui.password_input.text() != self.data["password"]:
            self.ui.settings_warning_label.setText('WARNING! You have unsaved changes.')
            self.ui.settings_warning_label.setStyleSheet(u"color: rgb(255, 255, 255);\
            background-color: rgb(255, 152, 152);\
            border: 2px solid rgb(255, 98, 98);\
            border-radius: 8px;\
            padding: 6px;")
            self.ui.password_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border: 3px solid orange;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")
        else:
            self.ui.settings_warning_label.setText("")
            self.ui.settings_warning_label.setStyleSheet(u"")
            self.ui.password_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border-bottom: 3px solid #3B324E;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")
    
    def timeinterval_edited(self):
        if self.ui.timeinterval_spinbox.value() != self.data["time_interval"]:
            self.ui.settings_warning_label.setText('WARNING! You have unsaved changes.')
            self.ui.settings_warning_label.setStyleSheet(u"color: rgb(255, 255, 255);\
            background-color: rgb(255, 152, 152);\
            border: 2px solid rgb(255, 98, 98);\
            border-radius: 8px;\
            padding: 6px;")
            self.ui.timeinterval_spinbox.setStyleSheet(u"QSpinBox {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-top-left-radius: 15px;\n"
        "   border-bottom-left-radius: 15px;\n"
        "	border: 3px solid orange;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}")
        else:
            self.ui.settings_warning_label.setText("")
            self.ui.settings_warning_label.setStyleSheet(u"")
            self.ui.timeinterval_spinbox.setStyleSheet(u"QSpinBox {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-top-left-radius: 15px;\n"
        "	border-bottom-left-radius: 15px;\n"
        "	border-bottom: 3px solid #3B324E;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}")

    def subject_edited(self):
        if self.ui.subject_input.text() != self.data["subject"]:
            self.ui.settings_warning_label.setText('WARNING! You have unsaved changes.')
            self.ui.settings_warning_label.setStyleSheet(u"color: rgb(255, 255, 255);\
            background-color: rgb(255, 152, 152);\
            border: 2px solid rgb(255, 98, 98);\
            border-radius: 8px;\
            padding: 6px;")
            self.ui.subject_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border: 3px solid orange;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")
        else:
            self.ui.settings_warning_label.setText("")
            self.ui.settings_warning_label.setStyleSheet(u"")
            self.ui.subject_input.setStyleSheet(u"QLineEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border-bottom: 3px solid #3B324E;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")

    def content_edited(self):
        if self.ui.content_input.toPlainText() != self.data["content"]:
            self.ui.settings_warning_label.setText('WARNING! You have unsaved changes.')
            self.ui.settings_warning_label.setStyleSheet(u"color: rgb(255, 255, 255);\
            background-color: rgb(255, 152, 152);\
            border: 2px solid rgb(255, 98, 98);\
            border-radius: 8px;\
            padding: 6px;")
            self.ui.content_input.setStyleSheet(u"QTextEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border: 3px solid orange;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")
        else:
            self.ui.settings_warning_label.setText("")
            self.ui.settings_warning_label.setStyleSheet(u"")
            self.ui.content_input.setStyleSheet(u"QTextEdit {\n"
        "	background-color: #fff;\n"
        "	padding: 8px;\n"
        "	border-radius: 15px;\n"
        "	border-bottom: 3px solid #3B324E;\n"
        "	font: 25 9pt \"Bahnschrift Light\";\n"
        "}\n")

    def complete(self):
        self.ui.sending_label.setText('')
        self.ui.sendingemail_label.setText('Done!')
        self.ui.emaillist_input.setReadOnly(False)
        self.ui.send_button.setDisabled(False)

    def update_email(self, email):
        self.ui.sendingemail_label.setText(email)

    def send_pressed(self, data, filename='config.json'):
        self.data["emails"] = self.ui.emaillist_input.toPlainText()
        with open('config.json', 'w') as f:
            json.dump(self.data, f, indent=4)
        emails = self.data["emails"].split('\n')
        self.ui.emaillist_input.setReadOnly(True)
        self.ui.send_button.setDisabled(True)
        self.ui.sending_label.setText('Sending Email to:')
        self.worker = send_worker.WorkerThread(emails=emails, user=self.data["email"],\
                password=self.data['password'], time_interval=self.data["time_interval"],\
                subject=self.data["subject"], content=self.data["content"])
        self.worker.start()
        self.worker.update_email.connect(self.update_email)
        self.worker.complete.connect(self.complete)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

