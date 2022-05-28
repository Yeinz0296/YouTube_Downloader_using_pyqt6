import sys
from pytube import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

# link = 'https://youtu.be/qOXDoYUgNlU'

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Youtube Downloader by Hazrien')
        self.setWindowIcon(QIcon('project/03_youtube_downloader/icon/noun-youtube-3451621.png'))
        self.resize(852, 480) #widht height
        
        # input URL
        self.input_url = QLineEdit(self)
        self.input_url.setGeometry(10,10,300,50)

        # display info
        self.display_data = QTextEdit(self)
        self.display_data.setGeometry(420,10, 400, 400)

        # Button
        self.button_fetch_data()
        self.button_download()

        # Path

    def button_fetch_data(self):
        button = QPushButton('Fetch Data', self)
        button.setGeometry(310,10,100,50)
        button.clicked.connect(self.button_click_fetch_data)
    
    def button_download(self):
        button = QPushButton('Download', self)
        button.setGeometry(10,200,400,50)
        button.clicked.connect(self.button_click_download)

    def button_click_fetch_data(self):
        global yt
        yt = YouTube(self.input_url.text())
        thumbnail = yt.thumbnail_url

        self.display_data.setPlainText(
            'Title: ' + yt.title + '\n' + 'Author: '+ yt.author 
        )
    
    def button_click_download(self):
        yt = YouTube(self.input_url.text())
        ys = yt.streams.get_highest_resolution()
        ys.download('project/03_youtube_downloader/download')

        if ys.on_complete:
            self.display_data.setPlainText(
                'Download Complete'
            )

  
# MAIN
app = QApplication(sys.argv)

window = MyApp()
window.show()

sys.exit(app.exec())
