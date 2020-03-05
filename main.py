from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QComboBox, QLabel, QFileDialog, QPushButton
from PyQt5.QtGui import QPixmap
from new import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.background()
        self.ui.setupUi(self)
        self.comboBox()
        self.file_entered()

    def background(self):
        label = QLabel(self)
        label.setGeometry(0,0,340,480)
        pixmap = QPixmap('2.png')
        label.setPixmap(pixmap)    


    def comboBox(self):
        combo = QComboBox(self)
        combo.addItems(["Архивировать", "Разархивировать"])
        combo.setFixedSize(150, 40)
        combo.move(50, 50)
        self.show()

    def file_entered(self):
        openfile = QPushButton('adsas', self)
        openfile.move(100,70)
        openfile.clicked.connect(self.showDialog)
        
        self.show()
    
    def showDialog():
        pass


    


        

 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())