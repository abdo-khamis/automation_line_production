from PySide6 import QtWidgets
from lib.init import *  
  
class AdminPanal(QtWidgets.QWidget):
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        
        v_layout = QtWidgets.QVBoxLayout()
        
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
        
        # Users and access to remove and add
        h_acc_btns =QtWidgets.QVBoxLayout()
        
        
        h_acc_btns.addStretch()
        
        h1 = QtWidgets.QHBoxLayout()
        h1.addStretch()
        self.show_users_btn = QtWidgets.QPushButton("Show Access Users")
        self.show_users_btn.setFixedSize(240,60)
        self.show_users_btn.setFont(font)
        self.show_users_btn.setStyleSheet(btn_style)
        self.show_users_btn.clicked.connect(self.show_users)
        h1.addWidget(self.show_users_btn)
        h1.addStretch()
        
        h_acc_btns.addLayout(h1)
        
        h2 = QtWidgets.QHBoxLayout()
        h2.addStretch()        
        self.tasks_btn = QtWidgets.QPushButton("Tasks")
        self.tasks_btn.setFixedSize(240,60)
        self.tasks_btn.setFont(font)
        self.tasks_btn.setStyleSheet(btn_style)
        self.tasks_btn.clicked.connect(self.task_sh) # edit here function
        h2.addWidget(self.tasks_btn)
        h2.addStretch()
        
        h_acc_btns.addLayout(h2)        

        h3 = QtWidgets.QHBoxLayout()
        h3.addStretch()  
        self.setting_btn = QtWidgets.QPushButton("Settings")
        self.setting_btn.setFixedSize(240,60)
        self.setting_btn.setFont(font)
        self.setting_btn.setStyleSheet(btn_style)
        self.setting_btn.clicked.connect(self.settings_sh)         
        h3.addWidget(self.setting_btn)
        h3.addStretch()
        
        h_acc_btns.addLayout(h3)         
      
  
        
        h_acc_btns.addStretch()
        
        
        
        
        
        v_layout.addLayout(h_r_l)
        
        v_layout.addStretch()
        v_layout.addLayout(h_acc_btns)
        v_layout.addStretch()
        
        
        self.setLayout(v_layout)
    
    @QtCore.Slot(int)
    def return_home(self):
        self.main_window.go_to_home()
    @QtCore.Slot(int)
    def show_users(self):
        self.main_window.show_users_p()       
    @QtCore.Slot(int)
    def settings_sh(self):
        self.main_window.settings_p()     
    
    @QtCore.Slot(int)
    def task_sh(self):
        self.main_window.taskPage()  
    