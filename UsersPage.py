from PySide6 import QtWidgets
from lib.init import *
from Dialogs.EditUserDia import *

class UsersPage(QtWidgets.QWidget):
    add_clicked = None
    def __init__(self,main_window, isShow = False):
        
        self.isShow = isShow
        
        
        super().__init__()
        self.main_window = main_window
        
        self.main_control = QtWidgets.QHBoxLayout()
        
        self.main_control.addStretch()
        
        self.add_user_btn = QtWidgets.QPushButton("Add Access")
        self.add_user_btn.setFixedSize(240, 50)
        self.add_user_btn.setFont(font)
        self.add_user_btn.setStyleSheet(btn_style)
        self.add_user_btn.clicked.connect(self.add_btn)
        
        self.main_control.addWidget(self.add_user_btn)
        self.main_control.addStretch()
        # return btn 
        self.return_btn = QtWidgets.QPushButton(">")
        self.return_btn.setFixedSize(50,50)
        self.return_btn.setStyleSheet(btn_style)
        self.return_btn.setFont(font)
        self.return_btn.clicked.connect(self.return_home)
        self.main_control.addWidget(self.return_btn)
        
        
        self.v_layout = QtWidgets.QVBoxLayout()
        
        #add_boxes
        self.h_add = QtWidgets.QHBoxLayout()
        self.username = QtWidgets.QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setFixedSize(200,50)
        self.username.setStyleSheet("background-color: #ffffff;")
        
        self.h_add.addWidget(self.username)
        
        self.password = QtWidgets.QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setFixedSize(200,50)
        self.password.setStyleSheet("background-color: #ffffff;")     
        
        self.h_add.addWidget(self.password)
        
        self.role = QtWidgets.QLineEdit()
        self.role.setPlaceholderText("Role")
        self.role.setFixedSize(200,50)
        self.role.setStyleSheet("background-color: #ffffff;")    
        
        self.h_add.addWidget(self.role)
        
        self.submit_btn = QtWidgets.QPushButton("Submit")
        self.submit_btn.setFixedSize(200, 50)
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet(btn_style)
        self.submit_btn.clicked.connect(self.submit)
        self.h_add.addWidget(self.submit_btn)
        
        for i in range(self.h_add.count()):
            item = self.h_add.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.hide()

        
        
        # stopped here 
        
        self.v_layout.addLayout(self.main_control)
        
        
        self.v_layout.addLayout(self.h_add)
        
        
        if self.isShow:
            self.show_users()
        
        
        self.setLayout(self.v_layout)
     
    def submit(self):
        
        isSuccess = AddAcess(self.username.text(), self.password.text(), self.role.text())
        
        if isSuccess:
            self.main_window.show_users_p()
        else:
            print("username is exist")
            
    def remove_access(self, username):
        isSuccess = RemoveAccess(username)
        
        if isSuccess:
            self.main_window.show_users_p()
        else:
            print("error")
    
    def edit_access(self,username):
        dialog = EditAccessDialog(username)
        
        if dialog.exec():
            pass
    
    def add_btn(self):
        if not self.add_clicked:
            self.add_clicked = True
            
            for i in range(self.h_add.count()):
                item = self.h_add.itemAt(i)
                widget = item.widget()
                if widget is not None:
                    widget.show()
        else:
            self.add_clicked = False
            for i in range(self.h_add.count()):
                item = self.h_add.itemAt(i)
                widget = item.widget()
                if widget is not None:
                    widget.hide()
            
     
    def show_users(self):   
        users = db_cr.execute("select * from users").fetchall()
        
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        container = QtWidgets.QWidget()
        container_layout = QtWidgets.QVBoxLayout(container)
        for user in users:
            
            frame = QtWidgets.QFrame()
            frame.setFixedHeight(100)
            frame.setStyleSheet("""
                                QFrame {
                                    background-color: white;
                                    border-radius: 8px;
                                    padding: 10px;
                                }
                                """)
            
            h_l = QtWidgets.QHBoxLayout()
            index = QtWidgets.QLabel(str(user[0]))
            h_l.addWidget(index)
            name = QtWidgets.QLabel(user[1])
            h_l.addWidget(name)
            role = QtWidgets.QLabel(user[3])
            h_l.addWidget(role)
            device_info = QtWidgets.QLabel(user[4])
            h_l.addWidget(device_info)
            last_access = QtWidgets.QLabel(user[-1])
            h_l.addWidget(last_access)
            
            btn_edit = QtWidgets.QPushButton("Edit")
            btn_edit.setFixedSize(100, 50)
            btn_edit.setStyleSheet(btn_style)
            btn_edit.clicked.connect(lambda _, u=user[1]: self.edit_access(u))


            h_l_btns = QtWidgets.QHBoxLayout()
            h_l_btns.addWidget(btn_edit)
            
            if user[1] == self.main_window.current_user[1] or user[3] == "owner":
                h_l.addSpacing(100)
                pass
            else:
                btn_remove = QtWidgets.QPushButton("Remove")
                btn_remove.setFixedSize(100, 50)
                btn_remove.setStyleSheet(btn_style)   
                btn_remove.clicked.connect(lambda _, u=user[1]: self.remove_access(u))

                h_l_btns.addWidget(btn_remove)
                
            h_l.addItem(h_l_btns)
            
            
                   
            
            
            frame_layout = QtWidgets.QVBoxLayout()
            frame_layout.addLayout(h_l)
            frame.setLayout(frame_layout)
            container_layout.addWidget(frame)
            
            
        scroll_area.setWidget(container)
        self.v_layout.addWidget(scroll_area)
            
    @QtCore.Slot(int)
    def return_home(self):
        self.main_window.go_to_adminP() 