import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PMGui as Ui

if __name__ == "__main__":

    # Create PyQt Application and Window
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    # Create instance of the UI class
    ui = Ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.setWindowTitle("Password Manager")

    MainWindow.show()
    sys.exit(app.exec_())
