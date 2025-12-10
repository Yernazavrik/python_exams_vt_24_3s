import PyQt5
import sys
from PyQt5 import QtWidgets
import json
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget()
        self.v_layout= QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.v_layout)
        self.text_line = QtWidgets.QLineEdit()
        self.text_line.setPlaceholderText("Поле ввода фильтра")
        self.v_layout.addWidget(self.text_line)
        self.send_button = QtWidgets.QPushButton("Use")
        self.send_button.setStyleSheet("background-color: green")
        self.check_box = QtWidgets.QCheckBox("Учитывать регистр")
        self.v_layout.addWidget(self.check_box)
        self.check_box.stateChanged.connect(self.change)
        self.v_layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.onClicked)
        self.label = QtWidgets.QLabel()
        self.v_layout.addWidget(self.label)
        self.setCentralWidget(self.widget)
        data_list = {}
        with open('users.json', 'r') as f:
            data_list = json.load(f)
        
        self.data_list = data_list
        print("ASdqsddsa: ", self.data_list)
    def change(self, state):
        if state == Qt.Checked:
            self.send_button.setStyleSheet("background-color: red")
            
        else:
            self.send_button.setStyleSheet("background-color: green")
    def onClicked(self, state):
        if state == Qt.Checked:    
            if user.startswith(self.text_line.text()):
                    self.label.setText(user)
        else:
            for user in self.data_list.get('users'):
                if self.text_line.text().lower()in user.lower():
                    self.label.setText(user)
            
            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()