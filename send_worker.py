from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import time
import yagmail

class WorkerThread(QThread):
    update_email = Signal(str)
    complete = Signal()
    def __init__(self, emails, user, password,time_interval, subject, content) -> None:
        super().__init__()
        self.emails = emails
        self.user = user
        self.password = password
        self.time_interval = time_interval
        self.subject = subject
        self.content = content
        self.yag = yagmail.SMTP(user=self.user, password=self.password)

    def run(self) -> None:  
        for email in self.emails:
            self.update_email.emit(email)
            self.yag.send(to=email, subject=self.subject, contents=self.content)
            time.sleep(self.time_interval)
        self.complete.emit()