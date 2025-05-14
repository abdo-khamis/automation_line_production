from PySide6 import QtWidgets
from lib.init import *  

class TasksPage(QtWidgets.QWidget):
    
    def __init__(self, main_window):
        
        super().__init__()
              
        self.main_window  = main_window 
                
        self.vertical_layout = QtWidgets.QVBoxLayout()
        
        
                # return btn 
        h_r_l = QtWidgets.QHBoxLayout()
        h_r_l.addStretch()
        h_r_l.addStretch()
        self.return_btn = QtWidgets.QPushButton(">")
        self.return_btn.setFixedSize(50,50)
        self.return_btn.setStyleSheet(btn_style)
        self.return_btn.setFont(font)
        self.return_btn.clicked.connect(self.return_home)
        h_r_l.addWidget(self.return_btn)
        
        
        self.vertical_layout.addLayout(h_r_l)    
        
        
        
        self.vertical_layout.addStretch()
        
        
        
        hori = QtWidgets.QHBoxLayout()
        hori.addStretch()
        
        
        text = QtWidgets.QLabel("Will Be Added in Future....")
        text.setFont(font)
        hori.addWidget(text)
        
        hori.addStretch()
        

        
        self.vertical_layout.addLayout(hori)
    
        self.vertical_layout.addStretch()
    
        self.setLayout(self.vertical_layout)
        
        
        
        
    @QtCore.Slot(int)
    def return_home(self):
        self.main_window.go_to_adminP()