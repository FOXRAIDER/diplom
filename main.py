from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QComboBox, QLabel, QFileDialog, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from new import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.window()
        self.background()
        self.settings()
        self.continue_btn()
        self.brand_name()
        self.ui.setupUi(self)
        self.logo()
        self.comboBox()
        self.enter_file()

    def window(self):
        #QtWidgets.QMainWindow.setFixedSize(320,480)
        main = QtWidgets.QMainWindow
        main.setFixedSize(self,320,480)

    def background(self):
        label = QLabel(self)
        label.setGeometry(0,0,340,480)
        label.setStyleSheet("background-color: rgb(42, 42, 42);") 
        #pixmap = QPixmap('2.png')
        #label.setPixmap(pixmap)    

    def logo(self):
        lbl = QLabel(self)
        lbl.setGeometry(85,70,150,150)
        pixmap = QPixmap('img/logo.png')
        lbl.setPixmap((pixmap))
        lbl.setScaledContents(1)    

    def comboBox(self):
        combo = QComboBox(self)
        combo.addItems(["COMPRESS", "DECOMPRESS"])
        combo.setFixedSize(150, 30)
        combo.move(85, 350)
        combo.activated[str].connect(self.onActivated)  
        default = "Архивировать"
        print(type(default))
    
    def settings(self):
        btn = QPushButton(self)
        btn.resize(50,480)
        btn.move(0,0)
        btn.setIcon(QIcon('img/settings.png'))
        btn.setIconSize(QSize(500,500))


    def continue_btn(self):
        btn = QPushButton(self)
        btn.resize(50,480)
        btn.move(270,0)
        btn.setIcon(QIcon('img/cont.png'))
        btn.setIconSize(QSize(500,500))
    
    def brand_name(self):
        temp = QLabel(self)
        temp.setGeometry(100,10,120,40)
        #temp.setStyleSheet("background-color: rgb(255, 255, 255);") 


    def enter_file(self):
        openfile = QPushButton(self)
        openfile.clicked.connect(self.showDialog)
        openfile.move(85,420)
        openfile.resize(150, 25)
        openfile.setIcon(QIcon('img/OPEN.png'))
        openfile.setIconSize(QSize(150,150))
        self.show()
    
    def showDialog(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')[0]

        fq = open(file, 'r')

        with fq:
            data = fq.read()
            print(data)

    def onActivated(self,text):
        if text is not None:
            print(type(text))
            
        else:
            print('error')
    




    


        

 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())