from PySide6 import QtWidgets
from lib.init import *  
from qasync import asyncSlot

class ControlWidget(QtWidgets.QWidget):
    def __init__(self, main_window, ws_listener):
        super().__init__()

        self.main_window = main_window
        
        self.ws = ws_listener
        
        
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
        
        
        h_lbl1 = QtWidgets.QHBoxLayout()
        h_lbl1.addStretch()
        lbl_1 = QtWidgets.QLabel("Manual Control")
        lbl_1.setFont(font)
        lbl_1.setFixedHeight(50)
        h_lbl1.addWidget(lbl_1)
        h_lbl1.addStretch()
        
        
        
        h_lbl2 = QtWidgets.QHBoxLayout()
        h_lbl2.addStretch()
        lbl_2 = QtWidgets.QLabel("Automatic Control")
        lbl_2.setFont(font)
        lbl_2.setFixedHeight(50)
        h_lbl2.addWidget(lbl_2)
        h_lbl2.addStretch()
        
        
        
        self.slider_grip = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.slider_grip.setRange(0, 180)
        self.slider_grip.setValue(90)
        # self.slider_grip.setDisabled(True)
        ws_listener.grip_value.connect(self.slider_grip.setValue)
        # self.slider_grip.setStyleSheet(slider_style)

        self.slider_shoulder = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.slider_shoulder.setRange(0, 180)
        self.slider_shoulder.setValue(90)
        # self.slider_shoulder.setDisabled(True)
        ws_listener.shoulder_value.connect(self.slider_shoulder.setValue)
        # self.slider_shoulder.setStyleSheet(slider_style)
        
        
        self.slider_elbow = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.slider_elbow.setRange(0, 180)
        self.slider_elbow.setValue(90)
        # self.slider_elbow.setDisabled(True)
        ws_listener.elbow_value.connect(self.slider_elbow.setValue)
        
        self.slider_base = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.slider_base.setRange(0, 180)
        self.slider_base.setValue(90)
        # self.slider_base.setDisabled(True)
        ws_listener.base_value.connect(self.slider_base.setValue)
        

        self.label_grip_title = QtWidgets.QLabel("Gripper", alignment=QtCore.Qt.AlignCenter)
        self.label_shoulder_title = QtWidgets.QLabel("Shoulder", alignment=QtCore.Qt.AlignCenter)
        self.label_elbow_title = QtWidgets.QLabel("Elbow", alignment=QtCore.Qt.AlignCenter)
        self.label_base_title = QtWidgets.QLabel("Base", alignment=QtCore.Qt.AlignCenter)



        self.label_grip_value = QtWidgets.QLabel(f"Current Position: {self.slider_grip.value()}")
        self.label_shoulder_value = QtWidgets.QLabel(f"Current Position: {self.slider_shoulder.value()}")
        self.label_elbow_value = QtWidgets.QLabel(f"Current Position: {self.slider_elbow.value()}")
        self.label_base_value = QtWidgets.QLabel(f"Current Position: {self.slider_base.value()}")
        

        self.slider_grip.valueChanged.connect(self.update_grip_label)
        self.slider_shoulder.valueChanged.connect(self.update_shoulder_label)
        self.slider_elbow.valueChanged.connect(self.update_elbow_label)
        self.slider_base.valueChanged.connect(self.update_base_label)
        

        layout = QtWidgets.QFormLayout()
        self.setLayout(layout)

        layout.addRow(h_r_l)
        layout.addRow(h_lbl1)
        layout.addRow(self.label_grip_title)
        layout.addRow(self.label_grip_value)
        layout.addRow(self.slider_grip)
        layout.addRow(self.label_shoulder_title)
        layout.addRow(self.label_shoulder_value)
        layout.addRow(self.slider_shoulder)
        layout.addRow(self.label_elbow_title)
        layout.addRow(self.label_elbow_value)
        layout.addRow(self.slider_elbow)
        layout.addRow(self.label_base_title)
        layout.addRow(self.label_base_value)
        layout.addRow(self.slider_base)
        
        layout.addRow(h_lbl2)
        
        
        self.start_button = QtWidgets.QPushButton("Start Belt")
        self.start_button.setFixedSize(240,60)
        self.start_button.clicked.connect(self.start)
        self.start_button.setStyleSheet(btn_style)
        self.start_button.setFont(font)
        

        
        self.stop_button = QtWidgets.QPushButton("Stop Belt")
        self.stop_button.hide()
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setFixedSize(240,60)
        self.stop_button.setStyleSheet(btn_style)
        self.stop_button.setFont(font)      
        
        self.clam_fn_btn = QtWidgets.QPushButton("Clamiping Function")
        self.clam_fn_btn.clicked.connect(self.ClamFn)
        self.clam_fn_btn.setFixedSize(240,60)
        self.clam_fn_btn.setStyleSheet(btn_style)
        self.clam_fn_btn.setFont(font)    
        
        
        h_layout = QtWidgets.QHBoxLayout()
        
        h_layout.addStretch()
        h_layout.addWidget(self.start_button)
        h_layout.addWidget(self.stop_button)
        h_layout.addWidget(self.clam_fn_btn)
        h_layout.addStretch()
        
        
        layout.addRow(h_layout)
        

        
        h_lbl3 = QtWidgets.QHBoxLayout()
        h_lbl3.addStretch()
        lbl_3 = QtWidgets.QLabel("Status")
        lbl_3.setFont(font)
        lbl_3.setFixedHeight(50)
        h_lbl3.addWidget(lbl_3)
        h_lbl3.addStretch()
        
        
        layout.addRow(h_lbl3)
        
        
        
        
        h_lbl4 = QtWidgets.QHBoxLayout()
        h_lbl4.addStretch()
        lbl_4 = QtWidgets.QLabel("History Data")
        lbl_4.setFont(font)
        lbl_4.setFixedHeight(50)
        h_lbl4.addWidget(lbl_4)
        h_lbl4.addStretch()
    
        layout.addRow(h_lbl4)


        h_lbl5 = QtWidgets.QHBoxLayout()
        h_lbl5.addStretch()
        lbl_5 = QtWidgets.QLabel("Database Settings")
        lbl_5.setFont(font)
        lbl_5.setFixedHeight(50)
        h_lbl5.addWidget(lbl_5)
        h_lbl5.addStretch()
    
        layout.addRow(h_lbl5)
        
        
        h_seet = QtWidgets.QHBoxLayout();h_seet.addStretch();copy_right = QtWidgets.QLabel(f"{app_copyright}");h_seet.addWidget(copy_right);h_seet.addStretch()
        layout.addRow(h_seet)
        
        
        

    @QtCore.Slot(int)
    def update_grip_label(self, value):
        self.label_grip_value.setText(f"Current Position: {value}")
        self.sendData("Gripper",value)

    @QtCore.Slot(int)
    def update_shoulder_label(self, value):
        self.label_shoulder_value.setText(f"Current Position: {value}")
        self.sendData("Shoulder",value)

    @QtCore.Slot(int)
    def update_elbow_label(self, value):
        self.label_elbow_value.setText(f"Current Position: {value}")
        self.sendData("Elbow",value)

    @QtCore.Slot(int)
    def update_base_label(self, value):
        self.label_base_value.setText(f"Current Position: {value}")
        self.sendData("Base",value)
        
    @QtCore.Slot(int)
    def return_home(self):
        self.main_window.go_to_home()
        
    @asyncSlot()
    async def sendData(self, key, value):
        if self.ws.websocket is not None:
            try:
                await self.ws.websocket.send(f"{key},{value}")
            except Exception as e:
                print(f"Send Error: {e}")

            
    @asyncSlot()  # ⬅ this makes the slot compatible with Qt signals
    async def start(self):
        if self.ws.websocket is not None:
            try:
                await self.ws.websocket.send("start, ON")
                print("start")
                self.stop_button.show()
                self.slider_base.setDisabled(True)
                self.slider_elbow.setDisabled(True)
                self.slider_grip.setDisabled(True)
                self.slider_shoulder.setDisabled(True)
                self.start_button.hide()
            except Exception as e:
                print(f"WebSocket Error: {e}")
    @asyncSlot()  # ⬅ this makes the slot compatible with Qt signals
    async def stop(self):
        if self.ws.websocket is not None:
            try:
                    await self.ws.websocket.send("stop, ON")
                    print("stop")
                    self.start_button.show()
                    self.slider_base.setDisabled(False)
                    self.slider_elbow.setDisabled(False)
                    self.slider_grip.setDisabled(False)
                    self.slider_shoulder.setDisabled(False)
                    self.stop_button.hide()
            except Exception as e:
                print(f"WebSocket Error: {e}")
    @asyncSlot()
    async def ClamFn(self):
        if self.ws.websocket is not None:
            try:
                await self.ws.websocket.send("automation_fn, ON")
            except Exception as e:
                print(e)
