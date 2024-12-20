# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import random
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1440, 834)
                MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label_smarthome = QtWidgets.QLabel(self.centralwidget)
                self.label_smarthome.setGeometry(QtCore.QRect(300, 10, 311, 101))
                font = QtGui.QFont()
                font.setPointSize(22)
                font.setBold(True)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                self.label_smarthome.setFont(font)
                self.label_smarthome.setStyleSheet("QLabel {\n"
        "color: white;  \n"
        "background-color: #3498db;  \n"
        "border-radius: 5px;  \n"
        "padding: 5px 10px;  \n"
        "border: 10px solid #000000;  \n"
        "\n"
        "}\n"
        "")
                self.label_smarthome.setObjectName("label_smarthome")
                self.label_hoten = QtWidgets.QLabel(self.centralwidget)
                self.label_hoten.setGeometry(QtCore.QRect(80, 680, 481, 81))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_hoten.setFont(font)
                self.label_hoten.setStyleSheet("QLabel {\n"
        "    background-color: #f0f0f0; \n"
        "    padding: 10px; \n"
        "    border: 6px solid #ccc; \n"
        "    border-radius: 30px;\n"
        "}\n"
        "")
                self.label_hoten.setObjectName("label_hoten")
                self.label_mssv = QtWidgets.QLabel(self.centralwidget)
                self.label_mssv.setGeometry(QtCore.QRect(830, 680, 331, 81))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label_mssv.setFont(font)
                self.label_mssv.setStyleSheet("QLabel {\n"
        "    background-color: #f0f0f0; \n"
        "    padding: 10px; \n"
        "    border: 6px solid #ccc; \n"
        "    border-radius: 30px;\n"
        "}\n"
        "")
                self.label_mssv.setObjectName("label_mssv")
                self.bt_on = QtWidgets.QPushButton(self.centralwidget)
                self.bt_on.setGeometry(QtCore.QRect(170, 200, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_on.setFont(font)
                self.bt_on.setMouseTracking(False)
                self.bt_on.setTabletTracking(False)
                self.bt_on.setAutoFillBackground(False)
                self.bt_on.setStyleSheet("QPushButton {\n"
        "    background-color:#5df564;\n"
        "    color: black; \n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px;\n"
        "\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:  #ed5ae3;\n"
        "}\n"
        "")
                self.bt_on.setCheckable(False)
                self.bt_on.setAutoRepeat(False)
                self.bt_on.setAutoDefault(False)
                self.bt_on.setObjectName("bt_on")
                self.bt_off = QtWidgets.QPushButton(self.centralwidget)
                self.bt_off.setGeometry(QtCore.QRect(290, 200, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_off.setFont(font)
                self.bt_off.setStyleSheet("QPushButton {\n"
        "    background-color: #ed0707;\n"
        "    color: black;\n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px; \n"
        "    border-radius:10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #ed5ae3;\n"
        "}\n"
        "")
                self.bt_off.setObjectName("bt_off")
                self.widget_fan = QtWidgets.QWidget(self.centralwidget)
                self.widget_fan.setGeometry(QtCore.QRect(610, 130, 171, 151))
                self.widget_fan.setStyleSheet("image: url(:/myimage/fan_1.png);\n"
        "background-color: rgb(170, 255, 255);")
                self.widget_fan.setObjectName("widget_fan")
                self.slider = QtWidgets.QSlider(self.centralwidget)
                self.slider.setGeometry(QtCore.QRect(200, 330, 160, 22))
                self.slider.setOrientation(QtCore.Qt.Horizontal)
                self.slider.setObjectName("slider")
                
                self.slider.setMinimum(0)  
                self.slider.setMaximum(100)  
                self.slider.setValue(0)
                self.slider.valueChanged.connect(self.update_label)
                self.bt_switch = QtWidgets.QPushButton(self.centralwidget)
                
                self.label_slider_value = QtWidgets.QLabel(self.centralwidget)
                self.label_slider_value.setGeometry(QtCore.QRect(180, 360, 160, 22))  
                self.label_slider_value.setObjectName("label_slider_value")
                self.label_slider_value.setText("Level: 0")
                self.label_slider_value.setStyleSheet("QLabel{\n"
    "   color: black;\n"
    "   background-color: transparent;\n"
    "   font-size: 14px;\n"
    "   font-weight: bold; \n"
    
    "}\n"
    "")
                self.bt_switch.setGeometry(QtCore.QRect(230, 430, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_switch.setFont(font)
                self.bt_switch.setMouseTracking(False)
                self.bt_switch.setTabletTracking(False)
                self.bt_switch.setAutoFillBackground(False)
                self.bt_switch.setStyleSheet("QPushButton {\n"
        "    background-color:#e321fc;\n"
        "    color: black; \n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px;\n"
        "\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:  #ed5ae3;\n"
        "}\n"
        "")
                self.bt_switch.setCheckable(False)
                self.bt_switch.setAutoRepeat(False)
                self.bt_switch.setAutoDefault(False)
                self.bt_switch.setObjectName("bt_switch")
                self.widget_lamp = QtWidgets.QWidget(self.centralwidget)
                self.widget_lamp.setGeometry(QtCore.QRect(610, 320, 171, 151))
                self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_1.png);\n"
        "background-color: rgb(170, 255, 255);")
                self.widget_lamp.setObjectName("widget_lamp")
                self.widget_tv = QtWidgets.QWidget(self.centralwidget)
                self.widget_tv.setGeometry(QtCore.QRect(610, 490, 171, 151))
                self.widget_tv.setStyleSheet("image: url(:/myimage/tv_1.png);\n"
        "background-color: rgb(170, 255, 255);")
                self.widget_tv.setObjectName("widget_tv")
                self.bieudo_1 = QtWidgets.QGraphicsView(self.centralwidget)
                self.bieudo_1.setGeometry(QtCore.QRect(900, 20, 431, 311))
                self.bieudo_1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.bieudo_1.setObjectName("bieudo_1")
                self.bieudo_2 = QtWidgets.QGraphicsView(self.centralwidget)
                self.bieudo_2.setGeometry(QtCore.QRect(900, 350, 431, 311))
                self.bieudo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.bieudo_2.setObjectName("bieudo_2")
                self.bt_mode1 = QtWidgets.QPushButton(self.centralwidget)
                self.bt_mode1.setGeometry(QtCore.QRect(80, 550, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_mode1.setFont(font)
                self.bt_mode1.setMouseTracking(False)
                self.bt_mode1.setTabletTracking(False)
                self.bt_mode1.setAutoFillBackground(False)
                self.bt_mode1.setStyleSheet("QPushButton {\n"
        "    background-color:#ffffff;\n"
        "    color: black; \n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px;\n"
        "\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:  #ed5ae3;\n"
        "}\n"
        "")
                self.bt_mode1.setCheckable(False)
                self.bt_mode1.setAutoRepeat(False)
                self.bt_mode1.setAutoDefault(False)
                self.bt_mode1.setObjectName("bt_mode1")
                self.bt_mode2 = QtWidgets.QPushButton(self.centralwidget)
                self.bt_mode2.setGeometry(QtCore.QRect(230, 550, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_mode2.setFont(font)
                self.bt_mode2.setMouseTracking(False)
                self.bt_mode2.setTabletTracking(False)
                self.bt_mode2.setAutoFillBackground(False)
                self.bt_mode2.setStyleSheet("QPushButton {\n"
        "    background-color:#ffffff;\n"
        "    color: black; \n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px;\n"
        "\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:  #ed5ae3;\n"
        "}\n"
        "")
                self.bt_mode2.setCheckable(False)
                self.bt_mode2.setAutoRepeat(False)
                self.bt_mode2.setAutoDefault(False)
                self.bt_mode2.setObjectName("bt_mode2")
                self.bt_clear = QtWidgets.QPushButton(self.centralwidget)
                self.bt_clear.setGeometry(QtCore.QRect(380, 550, 101, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.bt_clear.setFont(font)
                self.bt_clear.setMouseTracking(False)
                self.bt_clear.setTabletTracking(False)
                self.bt_clear.setAutoFillBackground(False)
                self.bt_clear.setStyleSheet("QPushButton {\n"
        "    background-color:#ffffff;\n"
        "    color: black; \n"
        "    border: 3px solid #000000;\n"
        "    padding: 10px;\n"
        "\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #07c7e0;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color:  #ed5ae3;\n"
        "}\n"
        "")
                self.bt_clear.setCheckable(False)
                self.bt_clear.setAutoRepeat(False)
                self.bt_clear.setAutoDefault(False)
                self.bt_clear.setObjectName("bt_clear")
                self.logo_t1 = QtWidgets.QWidget(self.centralwidget)
                self.logo_t1.setGeometry(QtCore.QRect(30, 10, 100, 100))
                self.logo_t1.setStyleSheet("image: url(:/myimage/logot1.png);\n"
        "background-color: rgb(0, 0, 0);")
                self.logo_t1.setObjectName("logo_t1")

                self.label_smarthome.raise_()
                self.label_hoten.raise_()
                self.label_mssv.raise_()
                self.bt_on.raise_()
                self.bt_off.raise_()
                self.widget_fan.raise_()
                self.slider.raise_()
                self.bt_switch.raise_()
                self.widget_lamp.raise_()
                self.widget_tv.raise_()
                self.bieudo_1.raise_()
                self.bieudo_2.raise_()
                self.bt_mode1.raise_()
                self.bt_mode2.raise_()
                self.bt_clear.raise_()
                self.logo_t1.raise_()

                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                
                self.fan_status = False
                self.lamp_status = False
                self.tv_status = False      
                self.current_device = "fan"
                self.bt_on.clicked.connect(self.turn_on)
                self.bt_off.clicked.connect(self.turn_off)
                self.bt_switch.clicked.connect(self.switch)
                self.bt_mode1.clicked.connect(self.mode1)
                self.bt_mode2.clicked.connect(self.mode2)
                self.bt_clear.clicked.connect(self.clear)
                self.timer = QtCore.QTimer()
                self.timer_1 = QtCore.QTimer()
                self.timer.timeout.connect(self.trangthai)
                self.timer_1.timeout.connect(self.trangthai_1)
                self.timer_1.timeout.connect(self.khoitaobieudo)
                self.chop_status = False
                self.chop_status_1 = False
                self.device_index = 0
                self.devices = ['fan', 'lamp', 'tv']

                self.figure_1 = Figure(figsize=(4, 3))
                self.canvas_1 = FigureCanvas(self.figure_1)
                self.axes_1 = self.figure_1.add_subplot(111)
                self.axes_1.set_title("Thiết Bị Hoạt Động")

                self.figure_2 = Figure(figsize=(4, 3))
                self.canvas_2 = FigureCanvas(self.figure_2)
                self.axes_2 = self.figure_2.add_subplot(111)
                self.axes_2.set_title("Năng Lượng Tiêu Thụ")

                self.chart_widget_1 = QtWidgets.QWidget(self.bieudo_1)
                self.chart_widget_2 = QtWidgets.QWidget(self.bieudo_2)

                self.layout_1 = QtWidgets.QVBoxLayout(self.chart_widget_1)
                self.layout_1.addWidget(self.canvas_1)

                self.layout_2 = QtWidgets.QVBoxLayout(self.chart_widget_2)
                self.layout_2.addWidget(self.canvas_2)
                self.bieudo_1.setLayout(self.layout_1)
                self.bieudo_2.setLayout(self.layout_2)

                self.fan_data = [1]
                self.lamp_data = [1]
                self.tv_data = [1]
                self.time_data = ["00:00:00"]

                self.bt_on.clicked.connect(self.khoitaobieudo)
                self.bt_off.clicked.connect(self.khoitaobieudo)
                self.bt_switch.clicked.connect(self.khoitaobieudo)
                self.slider.valueChanged.connect(self.khoitaobieudo)
                self.timer.timeout.connect(self.khoitaobieudo)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_smarthome.setText(_translate("MainWindow", "SMART HOME"))
                self.label_hoten.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">Họ và Tên: </span><span style=\" color:#ff5500;\">Phạm Thế Vinh</span></p></body></html>"))
                self.label_mssv.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">MSSV: </span><span style=\" color:#ff5500;\">21161388</span></p></body></html>"))
                self.bt_on.setText(_translate("MainWindow", "ON"))
                self.bt_off.setText(_translate("MainWindow", "OFF"))
                self.bt_switch.setText(_translate("MainWindow", "SWITCH"))
                self.bt_mode1.setText(_translate("MainWindow", "MODE 1"))
                self.bt_mode2.setText(_translate("MainWindow", "MODE 2"))
                self.bt_clear.setText(_translate("MainWindow", "CLEAR"))
        #level
        def set_fan_level(self, level):
                if level > 50:
                        self.widget_fan.setStyleSheet("image: url(:/myimage/fan_3.png);\n"
        "background-color: rgb(170, 255, 255);") 
                else:
                        self.widget_fan.setStyleSheet("image: url(:/myimage/fan_2.png);\n"
        "background-color: rgb(170, 255, 255);") 
        def set_lamp_level(self, level):
                if level > 50:
                        self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_3.png);\n"
        "background-color: rgb(170, 255, 255);")   
                else:
                        self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_2.png);\n"
        "background-color: rgb(170, 255, 255);")  
        def set_tv_level(self, level):
                if level > 50:
                        self.widget_tv.setStyleSheet("image: url(:/myimage/vt_3.png);\n"
        "background-color: rgb(170, 255, 255);") 
                else:
                        self.widget_tv.setStyleSheet("image: url(:/myimage/tv_2.png);\n"
        "background-color: rgb(170, 255, 255);")  
        #button
        def turn_on(self):
                if self.current_device == "fan":
                        self.fan_on(self.slider.value())  
                        self.update_label(self.slider.value())  
                elif self.current_device == "lamp":
                        self.lamp_on(self.slider.value())
                        self.update_label(self.slider.value())
                elif self.current_device == "tv":
                        self.tv_on(self.slider.value())
                        self.update_label(self.slider.value())
        def turn_off(self):
                if self.current_device == "fan":
                        self.fan_off()
                elif self.current_device == "lamp":
                        self.lamp_off()
                elif self.current_device == "tv":
                        self.tv_off()
        def switch(self):
                if self.current_device == "fan":
                        self.fan_status = False
                        self.current_device = "lamp" 
                elif self.current_device == "lamp":
                        self.lamp_status = False
                        self.current_device = "tv"  
                elif self.current_device == "tv":
                        self.tv_status = False
                        self.current_device = "fan"  
        #slider
        def update_label(self, value):
                self.label_slider_value.setText(""f"Level: {value}""")
                if self.current_device == "fan" and self.fan_status: 
                        if value > 50:
                                self.widget_fan.setStyleSheet("image: url(:/myimage/fan_3.png);\n"
        "background-color: rgb(170, 255, 255);") 
                        else:
                                self.widget_fan.setStyleSheet("image: url(:/myimage/fan_2.png);\n"
        "background-color: rgb(170, 255, 255);") 
                if self.current_device == "lamp" and self.lamp_status:  
                        if value > 50:
                                self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_3.png);\n"
        "background-color: rgb(170, 255, 255);") 
                        else:
                                self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_2.png);\n"
        "background-color: rgb(170, 255, 255);") 
                if self.current_device == "tv" and self.tv_status:  
                        if value > 50:
                                self.widget_tv.setStyleSheet("image: url(:/myimage/vt_3.png);\n"
        "background-color: rgb(170, 255, 255);") 
                        else:
                                self.widget_tv.setStyleSheet("image: url(:/myimage/tv_2.png);\n"
        "background-color: rgb(170, 255, 255);") 

                print("",value)
        #fan 
        def fan_on(self,level):
                self.fan_status = True
                self.set_fan_level(level) 
        def fan_off(self):
                self.widget_fan.setStyleSheet("image: url(:/myimage/fan_1);\n"
        "background-color: rgb(170, 255, 255);") 
                self.fan_status = False
        #lamp 
        def lamp_on(self,level):
                self.lamp_status = True
                self.set_lamp_level(level) 

        def lamp_off(self):
                self.widget_lamp.setStyleSheet("image: url(:/myimage/lamp_1);\n"
        "background-color: rgb(170, 255, 255);") 
                self.lamp_status = False
        #tv
        def tv_on(self,level):
                self.tv_status = True
                self.set_tv_level(level) 

        def tv_off(self):
                self.widget_tv.setStyleSheet("image: url(:/myimage/tv_1);\n"
        "background-color: rgb(170, 255, 255);") 
                self.tv_status = False
        #mode1
        def mode1(self):
                if self.timer.isActive():
                        self.timer.stop()  
                        self.turn_off_all()  
                        self.chop_status = False
                else:
                        self.timer.start(500)  
                        self.chop_status = True
                        self.timer_1.stop() 
                        self.chop_status_1 = False
        def trangthai(self):
                if self.chop_status:
                        if self.fan_status:
                                self.turn_off_all()  
                        else:
                                self.turn_on_all() 
        def turn_on_all(self):
                level = self.slider.value()
                self.fan_on(level)
                self.lamp_on(level)
                self.tv_on(level)
        def turn_off_all(self):
                self.fan_off()
                self.lamp_off()
                self.tv_off()
        #mode2
        def mode2(self):
                if self.timer_1.isActive():
                        self.timer_1.stop()
                        self.turn_off_all()
                        self.chop_status_1 = False
                else:
                        self.device_index = 0 
                        self.timer_1.start(300)  
                        self.chop_status_1 = True
                        self.timer.stop()
                        self.chop_status = False
        def trangthai_1(self):
                if self.chop_status_1:
                        self.turn_off_all() 
                        self.active()
        def active(self):
                if self.device_index < len(self.devices):
                        device = self.devices[self.device_index]
                        level = self.slider.value()
                        if device == 'fan':
                                self.fan_on(level)
                        elif device == 'lamp':
                                self.lamp_on(level)
                        elif device == 'tv':
                                self.tv_on(level)
                        self.device_index += 1  
                else:
                        self.device_index = 0
        def update_chart(self):
                current_time = datetime.now()
                formatted_time = current_time.strftime("%H:%M:%S")  
                self.time_data.append(formatted_time) 
                if len(self.time_data) > 3:  
                        self.time_data = self.time_data[-4:] 
                if self.fan_status:
                        self.fan_data.append(1)  
                else:
                        self.fan_data.append(0) 
                if len(self.fan_data) > 3:
                        self.fan_data = self.fan_data[-4:]
                if self.lamp_status:
                        self.lamp_data.append(1) 
                else:
                        self.lamp_data.append(0)  
                if len(self.lamp_data) > 3:
                        self.lamp_data = self.lamp_data[-4:]
                if self.tv_status:
                        self.tv_data.append(1)  
                else:
                        self.tv_data.append(0)  
                if len(self.tv_data) > 3:
                        self.tv_data = self.tv_data[-4:]
                print(formatted_time)
        def khoitaobieudo(self):
                self.update_chart()   
                self.update_chart_1()
                self.update_chart_2()
        def update_chart_1(self):
                self.axes_1.clear()  
                self.axes_1.set_xlabel("Thời Gian")
                self.axes_1.set_ylabel("Mức Hoạt Động")
                width = 0.2
                coso = random.randint(1, 3)
                x_indices = [i * (width*3 + 0.1) for i in range(len(self.time_data))]
                fan_data = [int(x+coso) for x in self.fan_data]
                lamp_data = [int((x+coso)*2) for x in self.lamp_data]
                tv_data = [int((x+coso)*3) for x in self.tv_data]
                self.axes_1.bar(x_indices, fan_data, width, label="Quạt")
                self.axes_1.bar([x + width for x in x_indices], lamp_data, width, label="Đèn")
                self.axes_1.bar([x + width * 2 for x in x_indices], tv_data, width, label="TV")
                print(fan_data,lamp_data,tv_data)
                if self.time_data: 
                        self.axes_1.set_xticks([x + width for x in x_indices])  
                        self.axes_1.set_xticklabels(self.time_data, ha="right")  
                self.axes_1.tick_params(axis="x", which="major", pad=5)
                self.axes_1.legend()
                self.canvas_1.draw() 
        def update_chart_2(self):
                self.axes_2.clear()
                self.axes_2.set_title("Năng Lượng Tiêu Thụ")
                nangluong_quat = sum(self.nangluong_quat(self.slider.value()) 
                        for i in range(len(self.time_data)) if self.fan_data[i] == 1)
                nangluong_den = sum(self.nangluong_den(self.slider.value()) 
                        for i in range(len(self.time_data)) if self.lamp_data[i] == 1)
                nangluong_tv = sum(self.nangluong_tv(self.slider.value()) 
                        for i in range(len(self.time_data)) if self.tv_data[i] == 1)
                nangluong_data = [nangluong_quat, nangluong_den, nangluong_tv]
                labels = ["Quạt", "Đèn", "TV"]
                colors = ["#3498db", "#e74c3c", "#f1c40f"]  
                if ((nangluong_quat == 0) and (nangluong_den == 0) and (nangluong_tv == 0)):
                        nangluong_data = [1,2,3]
                self.axes_2.pie(nangluong_data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
                self.canvas_2.draw()
                print(nangluong_data)
        def nangluong_quat(self, level):
                x = random.randint(3, 6) 
                nangluongtieuthu = (level+ x) * 15 
                thoigian = 1 / 3600  
                return nangluongtieuthu * thoigian 
        def nangluong_den(self, level):
                x = random.randint(1, 3) 
                nangluongtieuthu = (level+x) * 10 
                thoigian = 1 / 3600 
                return nangluongtieuthu * thoigian  
        def nangluong_tv(self, level):
                x = random.randint(6, 9) 
                nangluongtieuthu = (level+x) * 20 
                thoigian = 1 / 3600  
                return nangluongtieuthu * thoigian
        def clear(self):
                self.time_data = []
                self.fan_data = []
                self.lamp_data = []
                self.tv_data = []
                self.fan_status = False
                self.lamp_status = False
                self.tv_status = False
                self.current_device = "fan"
                self.set_fan_level(0)
                self.set_lamp_level(0)
                self.set_tv_level(0)
                self.update_label(0)
                self.timer.stop()
                self.timer_1.stop()
                self.chop_status = False
                self.chop_status_1 = False
                self.device_index = 0
                self.label_slider_value.hide()
                self.label_smarthome.hide()
                self.label_hoten.hide()
                self.label_mssv.hide()
                self.bt_on.hide()
                self.bt_off.hide()
                self.widget_fan.hide()
                self.slider.hide()
                self.bt_switch.hide()
                self.widget_lamp.hide()
                self.widget_tv.hide()
                self.bieudo_1.hide()
                self.bieudo_2.hide()
                self.bt_mode1.hide()
                self.bt_mode2.hide()
                self.bt_clear.hide() 
                self.logo_t1.hide()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
