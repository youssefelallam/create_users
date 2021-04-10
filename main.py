import os
import sys
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from int_ui import Ui_MainWindow


class MainApp(QMainWindow , Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.pushbutton()
    
    def handel_ui(self):
        self.setWindowTitle("User & Group")
        self.setFixedSize(440,397)
        self.setWindowIcon(QIcon("./icons/users.ico"))
    
    def pushbutton(self):
        self.pushButton.clicked.connect(self.creat_user)
        self.pushButton_2.clicked.connect(self.clear_user)
        self.pushButton_3.clicked.connect(self.creat_group)
        self.pushButton_4.clicked.connect(self.clear_group)

    def clear_user(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def clear_group(self):
        self.lineEdit_4.setText("")

        
    def creat_user(self):
        user = self.lineEdit.text()
        passw1 = self.lineEdit_2.text()
        passw2 = self.lineEdit_3.text()
        if passw1 != passw2:
            QMessageBox.warning(self, "Error", "the password is different")
        else:
            try:
                x = os.system(f'net user /add {user} {passw1}')
                if x != 0:
                    QMessageBox.warning(self, "Error", "run the program as administrator")
                else:
                    QMessageBox.information(self,"User","User created successfully")
                    self.clear_user()
            except:
                    QMessagebox.warning("error","you have a problem")

    def creat_group(self):
        group = self.lineEdit_4.text()
        try:
            y = os.system(f'net localgroup {group} /add')
            if y != 0:
                QMessageBox.warning(self, "Error", "run the program as administrator")
            else:
                QMessageBox.information(self,"Group","Group created successfully")
                self.clear_group()
        except:
            QMessagebox.warning("error","you have a problem")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
