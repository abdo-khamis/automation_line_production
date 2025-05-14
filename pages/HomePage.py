from PySide6 import QtWidgets
from lib.init import *  
        


class HomeWidget(QtWidgets.QWidget):
    
    def __init__(self, main_window, user):
        super().__init__()
        
        

            
        self.main_window = main_window

        vertical_layout = QtWidgets.QVBoxLayout()
        horizontal_layout= QtWidgets.QHBoxLayout()
        
        self.start_button = QtWidgets.QPushButton("Home")
        self.start_button.setFixedSize(240,60)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(btn_style)
 
        h_l = QtWidgets.QHBoxLayout()
        
        h_l.addStretch()
        
        self.hello_msg = QtWidgets.QLabel(f"Hello, ")
        self.hello_msg.setFont(font)
        self.hello_msg.setFixedHeight(50)
        h_l.addWidget(self.hello_msg)
        h_l.addStretch()
        
        
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.start_button)
        horizontal_layout.addStretch()
         
        vertical_layout.addStretch()
        vertical_layout.addLayout(h_l)
        vertical_layout.addLayout(horizontal_layout)

  
        
        if self.main_window.current_user[3] == "owner":
            h_l2= QtWidgets.QHBoxLayout()
            h_l2.addStretch()     
            self.admin_btn = QtWidgets.QPushButton("Admin Panal")
            self.admin_btn.setFixedSize(240,60)
            self.admin_btn.setFont(font)
            self.admin_btn.setStyleSheet(btn_style)       
            h_l2.addWidget(self.admin_btn)
            self.admin_btn.clicked.connect(self.admin_panal)
            h_l2.addStretch()
            vertical_layout.addLayout(h_l2)
        else:
          h_l2 = QtWidgets.QHBoxLayout()
          h_l2.addStretch()
          
          self.myTask_btn = QtWidgets.QPushButton("My Tasks")  
          self.myTask_btn.setFixedSize(240,60)
          self.myTask_btn.setFont(font)
          self.myTask_btn.setStyleSheet(btn_style)       
          h_l2.addWidget(self.myTask_btn)
          self.myTask_btn.clicked.connect(self.admin_panal)
          h_l2.addStretch()
          vertical_layout.addLayout(h_l2)       

        

        
        
        vertical_layout.addStretch()
        
        
        h_seet = QtWidgets.QHBoxLayout();h_seet.addStretch();copy_right = QtWidgets.QLabel(f"{app_copyright}");h_seet.addWidget(copy_right);h_seet.addStretch()
        
        vertical_layout.addLayout(h_seet)
        
        self.setLayout(vertical_layout)
        
        self.start_button.clicked.connect(self.home_p)
        
        
        
    def update_hello_msg(self):
        # This method is used to update the greeting message
        if self.main_window.current_user:
            self.hello_msg.setText(f"Hello, {self.main_window.current_user[1]}")
        else:
            self.hello_msg.setText("Hello, Guest")
        
        
    @QtCore.Slot(int)  # ⬅ this makes the slot compatible with Qt signals
    def home_p(self):
        self.main_window.go_to_control()
    @QtCore.Slot(int)
    def admin_panal(self):
        self.main_window.go_to_adminP()