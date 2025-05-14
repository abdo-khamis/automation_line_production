
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from PySide6.QtCore import Signal, QObject
from asyncio import *
import websockets as ws
from qasync import QEventLoop
from lib.init import *
from lib.automation import *


# pages

from pages.UsersPage import *
from pages.AdminPanel import *
from pages.LoginPage import *
from pages.HomePage import *
from pages.ControlPage import *
from pages.SettingsPage import *
from pages.TasksPage import *





class WebSocketListener(QObject):
    grip_value = Signal(int)
    shoulder_value = Signal(int)
    elbow_value = Signal(int)
    base_value = Signal(int)

    def __init__(self, url):
        super().__init__()
        self.url = url

    async def listen(self):
        self.arm_go_running = False
        try:
            async with ws.connect(self.url) as websocket:
                self.websocket = websocket
                
                while True:
                    msg = await websocket.recv()
                    
                    try:
                        if "Gripper" in str(msg):
                            self.grip_value.emit(int(msg.split(",")[1]))
                        elif "Shoulder" in str(msg):
                            self.shoulder_value.emit(int(msg.split(",")[1]))
                        elif "Elbow" in str(msg):    
                            self.elbow_value.emit(int(msg.split(",")[1]))
                        elif "Base" in str(msg):    
                            self.base_value.emit(int(msg.split(",")[1]))    
                        elif "arm_go" in str(msg):
                            asyncio.create_task(ArmGo(websocket))
                    except:
                        print('err')
        except ConnectionClosedError:
            
            print("WebSocket connection closed. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"WebSocket connection error: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)
        finally:
            if hasattr(self, 'websocket') and self.websocket and not self.websocket.closed:
                await self.websocket.close()
                print("WebSocket connection explicitly closed.")
            self.websocket = None









class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ws_listener):
        super().__init__()
        self.current_user = None
        self.ws_listener = ws_listener
        self.setWindowTitle(f"{app_name}")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #e8f2ff;")
        self.stack = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack)


        self.login = LoginPage(self)
        self.control = ControlWidget(self,self.ws_listener)
        
        
        self.stack.addWidget(self.login) # index 0
        self.stack.addWidget(self.control) # index 1


        self.stack.setCurrentIndex(0)  # Show HomeWidget

    def go_to_control(self):
        control_wd = self.control
        index = self.stack.indexOf(control_wd)
        self.stack.setCurrentIndex(index)
    def go_to_home(self):
        self.home = HomeWidget(self, self.current_user)
        self.home.update_hello_msg()
        home_wd = self.home
        self.stack.addWidget(self.home)
        index = self.stack.indexOf(home_wd)
        self.stack.setCurrentIndex(index)
    def go_to_adminP(self):
        self.admin_panal = AdminPanal(self)
        admin_wd = self.admin_panal
        self.stack.addWidget(self.admin_panal)
        index = self.stack.indexOf(admin_wd)
        self.stack.setCurrentIndex(index)
    def show_users_p(self):
        self.show_users_page = UsersPage(self,True)
        users_wd = self.show_users_page
        self.stack.addWidget(self.show_users_page)
        index = self.stack.indexOf(users_wd)
        self.stack.setCurrentIndex(index)
    def settings_p(self):
        self.settings_page = SettingsPage(self)
        settings_wd = self.settings_page
        self.stack.addWidget(self.settings_page)
        index = self.stack.indexOf(settings_wd)
        self.stack.setCurrentIndex(index)
        
    def taskPage(self):
        self.task_page = TasksPage(self)
        task_wd = self.task_page
        self.stack.addWidget(self.task_page)
        index = self.stack.indexOf(task_wd)
        self.stack.setCurrentIndex(index)

 
    
    
        


    

  
        
if __name__ == "__main__":

    
    app = QApplication([])
    loop = QEventLoop(app)
    set_event_loop(loop)

    listener = WebSocketListener(server_url)
    window = MainWindow(listener)
    window.show()
    
    loop.create_task(listener.listen())

    with loop:
        loop.run_forever()