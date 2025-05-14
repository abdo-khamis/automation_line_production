from PySide6.QtWidgets import QDialog
from lib.init import *


class ChangeServerDia(QDialog):
    def __init__(self, title, index):
        super().__init__()

        self.title = title

        
        self.setWindowTitle(f"Edit {title}")
        
        
        self.settings = db_cr.execute(f"select * from settings where id = 1").fetchone()


        

        # Create input field
        self.settings_edit = QtWidgets.QLineEdit()
        self.settings_edit.setText(self.settings[index])
        self.settings_edit.setPlaceholderText(f"{title}")
        


        # Create a submit button
        self.submit_btn = QtWidgets.QPushButton("Submit")
        self.submit_btn.clicked.connect(self.handle_submit)

        # Layout setup
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.settings_edit)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def handle_submit(self):
        settings_txt = self.settings_edit.text()
        
        if server_url:
            UpdateSettings(f'{self.title}', settings_txt)
            
                
        self.accept()