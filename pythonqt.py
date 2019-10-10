import sys

from PyQt5 import QtNetwork
from PyQt5.QtWidgets import (QApplication,
                             QLineEdit,
                             QMainWindow,
                             QPushButton,
                             QTextBrowser,)
from PyQt5.QtCore import (pyqtSlot,
                          QCoreApplication,
                          QUrl,)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setGeometry(20, 20, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(760, 30)

        self.button = QPushButton('Request', self)
        self.button.move(15, 60)
        self.button.resize(770, 40)

        self.textbrowser = QTextBrowser(self)
        self.textbrowser.move(20,105)
        self.textbrowser.resize(760, 480)

        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        url = self.textbox.text()

        request = QtNetwork.QNetworkRequest(QUrl(url))
        self.netaccessmngr = QtNetwork.QNetworkAccessManager()
        self.netaccessmngr.finished.connect(self.handle_response)
        self.netaccessmngr.get(request)

    def handle_response(self, reply):
        error_reply = reply.error()

        if error_reply == QtNetwork.QNetworkReply.NoError:
            bytes_string = reply.readAll()
            self.textbrowser.setText(str(bytes_string))
        else:
            self.textbrowser.setText(reply.errorString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
