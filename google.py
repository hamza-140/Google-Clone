import webbrowser
from PyQt6.QtWidgets import *
import sys
from PyQt6.QtGui import *


class Google(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowIcon(QIcon('images/google-logo.png'))
        self.search_box = None
        self.widget = QWidget()
        self.setWindowTitle("Google")
        self.setFixedSize(1150, 550)
        self.setStyleSheet("background-color:#fefefa ")
        self.top_buttons()
        self.name_image()
        self.search_area()
        self.search_icon()

    def name_image(self):
        label = QLabel(self)
        pixmap = QPixmap('images/google.png')
        label.setPixmap(pixmap)
        label.setFixedSize(280, 90)
        label.setFixedHeight(92)
        label.move(450, 120)

    def search_icon(self):
        label = QLabel(self)
        pixmap = QPixmap('images/search-icon.png')
        label.setPixmap(pixmap)
        label.setFixedSize(20, 20)
        label.move(800, 250)

    def search_area(self):
        self.search_box = QPlainTextEdit(self)
        self.search_box.setGeometry(330, 240, 500, 40)
        search_button = QPushButton("Google Search", self)
        search_button.clicked.connect(self.search)
        search_button.setStyleSheet("border-radius:5px;background-color:#f8f9fa")
        search_button.setGeometry(450, 300, 120, 30)
        feeling_button = QPushButton("I'm Feeling Lucky", self)
        feeling_button.clicked.connect(self.feeling)
        feeling_button.setGeometry(610, 300, 120, 30)
        feeling_button.setStyleSheet("border-radius:5px;background-color:#f8f9fa")
        self.search_box.setStyleSheet("border: 0.6px solid rgba(0,0,0,.3);border-radius:10px")

    def search(self):
        webbrowser.open('https://www.google.com/search?q=' + self.search_box.toPlainText())

    def feeling(self):
        webbrowser.open('https://www.google.com/doodles')

    def top_buttons(self):
        menu_bar = self.menuBar()
        menu_bar.addMenu("Gmail")
        menu_bar.addMenu("Images")
        options_label = QLabel(self)
        options = QPixmap('images/options.png')
        options_label.setPixmap(options)
        options_label.move(1070, 10)
        profile_img = QPixmap("images/mine.png")
        profile_label = QLabel(self)
        profile_label.setFixedSize(32, 32)
        profile_label.move(1100, 10)
        profile_label.setPixmap(profile_img)
        menu_bar.setStyleSheet("padding-left:950px;padding-top:15px;")


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
