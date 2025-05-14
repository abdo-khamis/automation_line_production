from PySide6 import QtWidgets
from lib.init import *  
from Dialogs.ChangeServerDia import *

class SettingsPage(QtWidgets.QWidget):
    
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
        
        
        h_acc_btns =QtWidgets.QVBoxLayout()
        
        
        h1 = QtWidgets.QHBoxLayout()
        h1.addStretch()
        self.app_n = QtWidgets.QPushButton("Change App Name")
        self.app_n.setFixedSize(300,60)
        self.app_n.setFont(font)
        self.app_n.setStyleSheet(btn_style)
        self.app_n.clicked.connect(lambda _, u='u_name' : self.update_settings(u))
        h1.addWidget(self.app_n)
        h1.addStretch()
    
    
        h2 = QtWidgets.QHBoxLayout()
        h2.addStretch()
        self.app_ver = QtWidgets.QPushButton("Change App Version")
        self.app_ver.setFixedSize(300,60)
        self.app_ver.setFont(font)
        self.app_ver.setStyleSheet(btn_style)
        self.app_ver.clicked.connect(lambda _, u='u_version' : self.update_settings(u))
        h2.addWidget(self.app_ver)
        h2.addStretch()
        
        h3 = QtWidgets.QHBoxLayout()
        h3.addStretch()        
        self.chng_serv = QtWidgets.QPushButton("Change Websocket Server")
        self.chng_serv.setFixedSize(300,60)
        self.chng_serv.setFont(font)
        self.chng_serv.setStyleSheet(btn_style)
        self.chng_serv.clicked.connect(lambda _, u='u_server' : self.update_settings(u))
        h3.addWidget(self.chng_serv)
        h3.addStretch()
        
        h4 = QtWidgets.QHBoxLayout()
        h4.addStretch()
        self.copri = QtWidgets.QPushButton("Change Copyright")
        self.copri.setFixedSize(300,60)
        self.copri.setFont(font)
        self.copri.setStyleSheet(btn_style)
        self.copri.clicked.connect(lambda _, u='u_copri' : self.update_settings(u))
        h4.addWidget(self.copri)
        h4.addStretch()  
        
        h_acc_btns.addStretch()
        h_acc_btns.addLayout(h1)
        h_acc_btns.addLayout(h2)
        h_acc_btns.addLayout(h3)
        h_acc_btns.addLayout(h4)
        
        h_acc_btns.addStretch()
        
        
        
        
        v_layout.addLayout(h_r_l)
        
        v_layout.addStretch()
        v_layout.addLayout(h_acc_btns)
        v_layout.addStretch()
        
        
        self.setLayout(v_layout)
    
    @QtCore.Slot(int)
    def return_home(self):
        self.main_window.go_to_adminP()
        
        
    def update_settings(self, task):
        
        if task == 'u_server':
            dialog = ChangeServerDia("server_url", 1)
        elif task == 'u_name':
            dialog = ChangeServerDia("app_name", 2)
        elif task == 'u_version':
            dialog = ChangeServerDia("app_version", 4)
        elif task == 'u_copri':
            dialog = ChangeServerDia("copyright", 3)
        
        if dialog.exec():
            pass
