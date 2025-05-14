import sqlite3 as sql
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import os
import platform
import datetime




# database path for exe app

def resource_path(relative_path):
    """Get the absolute path to the resources in the bundled app."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")  # Use current working directory for non-packaged version
    return os.path.join(base_path, relative_path)


# database and connections
db_path = resource_path("app.automation.db")
db = sql.connect(db_path)
db_cr = db.cursor()
user = []




def Login(username, password):
    
    db_cr.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user_data = db_cr.fetchone()
    if user_data:
        
        db_cr.execute(f'update users set device_name = "{platform.node()}", last_access = "{datetime.datetime.now().strftime(r"%H:%M %d-%m-%Y")}" where username = "{username}"')
        db.commit()
        
        # after update 
        db_cr.execute(f"SELECT * FROM users WHERE username = '{username}'")
        user_data_updated = db_cr.fetchone()
        return user_data_updated
    
def AddAcess(username, password, role):
    
    check_username = db_cr.execute(f"select * from users where username = '{username}'").fetchone()
    
    if check_username:
        return 0
    
    
    db_cr.execute(f"insert into users(username, password, role) values('{username}','{password}','{role}')")
    
    # print("success")
    db.commit()
    
    return 1     
   
def RemoveAccess(username):
    
    db_cr.execute(f"delete from users where username = '{username}'")
    
    db.commit()
    
    return 1

def EditUpdate(username, new_username=None, new_role=None):
    
    if not new_username and not new_role:
        pass
    elif not new_username and new_role:
        db_cr.execute(f"update users set role='{new_role}' where username = '{username}'")
    elif not new_role and new_username:
        db_cr.execute(f"update users set username = '{new_username}' where username = '{username}'")
        # db.commit()
    else:
        db_cr.execute(f"update users set username = '{new_username}', role='{new_role}' where username = '{username}'")
    
    db.commit()
    # print("here")
    
def UpdateSettings(field_name, new_val):
    
    getOldData = db_cr.execute(f"select {field_name} from settings where id = 1").fetchone()[0]
    
    if new_val == getOldData:
        
        return 0
    else:
        
        db_cr.execute(f"update settings set {field_name} = '{new_val}' where id=1")
        db.commit()
    
    
# get info from database 

SettingsData = db_cr.execute("select * from settings").fetchone()


# websocket server

server_url = f"ws://{SettingsData[1]}"
app_name = SettingsData[2]
app_version = SettingsData[4]
app_copyright = SettingsData[3]




    

# font and designs
font = QtGui.QFont()      
font.setFamily("Monospace")
font.setPointSize(15)       


btn_style = """
    QPushButton {
        background-color: #579af9;
        color: #ffffff;
        border: 2px solid transparent;  
        border-radius: 5px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #2e79e3;
        border-color: #ffffff;  
    }
"""


