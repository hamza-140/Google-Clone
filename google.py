from PyQt6.QtWidgets import *
import sys
from PyQt6.QtGui import *


class Google(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.search_box = None
        self.setWindowTitle("Google")
        self.setFixedSize(1150, 550)
        self.setStyleSheet("background-color:#fefefa ")
        self.top_buttons()
        # self.google_name()
        self.name_image()
        self.search_area()

    def name_image(self):
        label = QLabel(self)
        pixmap = QPixmap('google.png')
        label.setPixmap(pixmap)
        label.setFixedSize(280,90)
        label.setFixedHeight(92)
        label.move(400,120)

    def google_name(self):
        g = QLabel('G', self)
        g.setStyleSheet("color: blue")
        g.move(350,120)
        g.setFixedHeight(50)
        # g.setGeometry(350, 0, 60, 40)
        o1 = QLabel('o', self)
        o1.setStyleSheet("color: red")
        o1.move(430, 120)
        o1.setFixedHeight(50)
        # o.setGeometry(430, 100, 50, 60)
        o = QLabel('o', self)
        o.setStyleSheet("color: yellow")
        o.move(510, 120)
        o.setFixedHeight(50)
        # o.setGeometry(510, 100, 50, 60)
        g1 = QLabel('g', self)
        g1.setStyleSheet("color: blue")
        g1.move(590, 110)
        g1.setFixedHeight(80)
        # g.setGeometry(590, 100, 40, 70)
        l = QLabel('l', self)
        l.setStyleSheet("color: green")
        l.move(670, 120)
        l.setFixedHeight(50)
        # l.setGeometry(670, 100, 40, 60)
        e = QLabel('e', self)
        e.setStyleSheet("color: red")
        e.move(720, 120)
        e.setFixedHeight(50)
        # e.setGeometry(720, 100, 40, 60)

    def search_area(self):
        self.search_box = QTextEdit(self)
        self.search_box.setGeometry(300, 240, 500, 40)
        search_button = QPushButton("Google Search", self)
        search_button.setStyleSheet("border-radius:5px;background-color:#f8f9fa")
        search_button.setGeometry(420, 300, 120, 30)
        feeling_button = QPushButton("I'm Feeling Lucky", self)
        feeling_button.setGeometry(580, 300, 120, 30)
        feeling_button.setStyleSheet("border-radius:5px;background-color:#f8f9fa")
        search_button.clicked.connect(self.testing)
        self.search_box.setStyleSheet("border: 0.6px solid rgba(0,0,0,.3);border-radius:10px")

    def testing(self):
        print(self.search_box.toPlainText())

    def top_buttons(self):
        gmail = QLabel("Gmail",self)
        gmail.setStyleSheet("font-size:13px;font-weight:normal;color:rgba(0,0,0,.87)")
        gmail.move(1000,5)
        gmail.setObjectName("label")
        image = QLabel("Images", self)
        image.setStyleSheet("font-size:13px;font-weight:normal;color:rgba(0,0,0,.87)")
        image.move(1050, 5)


app = QApplication([])
app.setStyleSheet("""
            QLabel
            {
                font-size:60px;
                font-weight: bold;
            }
             """
                  )
window = Google()
window.show()
sys.exit(app.exec())
