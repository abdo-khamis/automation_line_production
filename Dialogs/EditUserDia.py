from PySide6.QtWidgets import QDialog
from lib.init import *


class EditAccessDialog(QDialog):
    def __init__(self, username):
        super().__init__()

        self.setWindowTitle("Edit Access")
        
        
        self.user = db_cr.execute(f"select * from users where username = '{username}'").fetchone()

        # Create input field
        self.username = QtWidgets.QLineEdit()
        self.username.setText(self.user[1])
        self.username.setPlaceholderText("Username")
        
        self.role = QtWidgets.QLineEdit()
        self.role.setText(self.user[3])


        # Create a submit button
        self.submit_btn = QtWidgets.QPushButton("Submit")
        self.submit_btn.clicked.connect(self.handle_submit)

        # Layout setup
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.username)
        layout.addWidget(self.role)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def handle_submit(self):
        username = self.username.text()
        role = self.role.text()
        
        if self.user[1] == username and self.user[3] != role:
            EditUpdate(self.user[1], new_role=role)
        elif self.user[1] != username and self.user[3] == role:
            EditUpdate(self.user[1], new_username=username)
        elif self.user[1] != username and self.user[3] != role:
            EditUpdate(self.user[1], new_role=role, new_username=username)
        else:
            # EditUpdate(self.username)
            pass
            
                
        self.accept()