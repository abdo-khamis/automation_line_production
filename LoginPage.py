from PySide6 import QtWidgets
from lib.init import *  


class LoginPage(QtWidgets.QWidget):
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addStretch()
        
        
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addStretch()
        self.label = QtWidgets.QLabel()
        # self.label.setFixedHeight(50)
        # self.label.setFont(font)
        
        self.logo = QtGui.QPixmap(resource_path("images/automation.png"))
        scaled = self.logo.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(scaled)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border: none; background: transparent;")
        h_layout.addWidget(self.label)
        
        h_layout.addStretch()
        
        v_layout.addLayout(h_layout)
        
        # v_layout.addStretch()    
        
        # username input    
        h_layout_username = QtWidgets.QHBoxLayout()
        h_layout_username.addStretch()
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setFixedSize(400,50)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("background-color: #ffffff;")
        self.username_input.setPlaceholderText("Enter Username")
        h_layout_username.addWidget(self.username_input)
        h_layout_username.addStretch()
        
        v_layout.addLayout(h_layout_username)
        
        # password input
        h_layout_password = QtWidgets.QHBoxLayout()
        h_layout_password.addStretch()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setFixedSize(400,50)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("background-color: #ffffff;")
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        h_layout_password.addWidget(self.password_input)
        h_layout_password.addStretch()        
        
        v_layout.addLayout(h_layout_password)
        
        # login_button
        h_layout_btn = QtWidgets.QHBoxLayout()
        h_layout_btn.addStretch()
        self.login_btn = QtWidgets.QPushButton("Access")
        self.login_btn.setFont(font)
        self.login_btn.setFixedSize(400,50)
        self.login_btn.setStyleSheet(btn_style)
        self.login_btn.clicked.connect(self.login)
        h_layout_btn.addWidget(self.login_btn)
        h_layout_btn.addStretch()
        
        
        h_err_mg = QtWidgets.QHBoxLayout()
        h_err_mg.addStretch()
        self.err_msg = QtWidgets.QLabel("Username or Password not correct!")
        self.err_msg.hide()
        self.err_msg.setStyleSheet("color: red;")
        h_err_mg.addWidget(self.err_msg)
        h_err_mg.addStretch()
        v_layout.addLayout(h_err_mg)
        
        v_layout.addLayout(h_layout_btn)
        
        
        v_layout.addStretch()
        
        h_seet = QtWidgets.QHBoxLayout();h_seet.addStretch();copy_right = QtWidgets.QLabel(f"{app_copyright}");h_seet.addWidget(copy_right);h_seet.addStretch()
        
        v_layout.addLayout(h_seet)
        
                
        self.setLayout(v_layout)
        # v_layout.addWidget(QtWidgets.QLabel("Login Page"))
        
    @QtCore.Slot(int)
    def login(self):
        
        user = Login(self.username_input.text(), self.password_input.text())
        
        if user:
            self.main_window.current_user = user
            print(self.main_window.current_user)
            self.main_window.go_to_home()
        else:
            self.err_msg.show()