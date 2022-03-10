from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
#from PySide2.QtWidgets import *
import sys
#import platform
import os
import socket
import time
import numpy as np
import threading
import numpy as np
from collections import deque

from SMS_script import send_SMS

import icons_rc
##GUI file
#from ui_Login_form import Ui_MainWindow
from ui_functions import *
#from ui_dashboard import Ui_Dashboard
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import datetime
## GLOBAL VARIABLES
water_level_current = 0
flow_rate_current = 0
temperature_current = 0
humidity_current = 0

fault_time = datetime.datetime.now()
current_time = datetime.datetime.now()
count = 0
servo_position = 0
string = ''
app = True
receiving = 'NULL'
opened = True
ip_address = '127.0.0.1'
number = 8374224474
port = 4450
name = 'Anik'
conn = 'NULL'
        


class Dashboard(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        socket_server = socket.socket()
        print('This is server/host IP address: ',ip_address)
        socket_server.bind((ip_address, port))
        print( "Binding successful!")
        print("This is your IP: ", ip_address)
        
        socket_server.listen()
        global conn
        conn, add = socket_server.accept()
        print(type(conn))
        print("connected")
        
        
##        self.ui = Ui_Dashboard()
##        self.ui.setupUi(self)

        self.ui = uic.loadUi("dashboard.ui",self)
        self.timestamp = 0
        self.time_axis = []
        self.water_level_axis = []
        self.graph_limit = 20
        self.traces = dict()
        self.deque_timestamp = deque([], maxlen=self.graph_limit+20)
        self.deque_water_level = deque([], maxlen=self.graph_limit+20)
        self.current_water_graph = None


        # Labelling plot

        self.waterflow_plot = PlotWidget()
        self.waterflow_plot.setBackground((39, 53, 69))
        x_axis = self.waterflow_plot.hideAxis('bottom')
        y_axis = self.waterflow_plot.hideAxis('left')

        self.ui.gridLayout.addWidget(self.waterflow_plot,0 ,0 , 1, 3)
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))



        
        # Transmitting data (Multithreaded process)
        self.transmit()
        
        #Receiving data from server
        print("Started")
        global receiving
        receiving = threading.Thread(target=self.start_rx)
        receiving.start()
        print("Started again")
##        self.timer_rx = QtCore.QTimer()
##        self.timer_rx.start(0)
##        self.timer_rx.timeout.connect(lambda: self.slider_update())
        


        
        self.show()
        

        # APPLY DROPSHADOW TO FRAME
        self.ui.frame.setGraphicsEffect(self.shadow)
        # MINIMIZE
        self.ui.Minimize.clicked.connect(lambda: self.min_window())

        # CLOSE
        self.ui.Close.clicked.connect(lambda: self.close_window())

        # Sending text

        self.ui.SOS_btn.clicked.connect(lambda: self.emergency_text())

        # Changing IP_address and port number on GUI

        
        ip_addr_text = """{IP_ADDR}"""
        newip = ip_addr_text.replace("{IP_ADDR}", str(ip_address))
        self.ui.IP_address.setText(newip)

        port_text = """{PORT}"""
        newport = port_text.replace("{PORT}", str(port))
        self.ui.Port.setText(newport)

        # Changing Name and number

        name_text = """{NAME}"""
        newname = name_text.replace("{NAME}", str(name))
        self.ui.Emergency_name.setText(newname)

        number_text = """{NUMBER}"""
        newnumber = number_text.replace("{NUMBER}", str(number))
        self.ui.Emergency_name_2.setText(newnumber)
        # Independent movement of window

        
            
        def moveWindow(event):
                
                
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

    def start_rx(self):
        global opened
        while opened:
            self.receive_data()
            print("Hello")
        
        
    def emergency_text(self):
        global water_level_current, flow_rate_current, temperature_current, humidity_current, number, fault_time, current_time
        send_SMS( flow_rate_current, water_level_current ,temperature_current, humidity_current, number)

        SMS_signal_stylesheet = """
        background-color: {COLOR};
        border-radius: 20px;
        """
        
        fault_time = datetime.datetime.now()
            
            
        new_SMS_signal_stylesheet = SMS_signal_stylesheet.replace("{COLOR}", "#ff9400")
        self.ui.SMS_signal.setStyleSheet(new_SMS_signal_stylesheet)

        self.timer_SMS = QtCore.QTimer()
        self.timer_SMS.start(0)
        self.timer_SMS.timeout.connect(lambda: self.change_alert_color(SMS_signal_stylesheet))


    def change_alert_color(self,SMS_signal_stylesheet):

        global fault_time, current_time
        current_time = datetime.datetime.now()
        
        time_diff = current_time - fault_time

        if time_diff >= datetime.timedelta(seconds=30):
            new_SMS_signal_stylesheet = SMS_signal_stylesheet.replace("{COLOR}", "#1a222f")
            self.ui.SMS_signal.setStyleSheet(new_SMS_signal_stylesheet)
            self.timer_SMS.stop()
                
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def min_window(self):
        self.showMinimized()
    def close_window(self):
        global receiving, opened
        opened = False
        receiving.join()
        print("closing")
        sys.exit()
        self.close()

    def receive_data(self):
        global app, string
        self.timestamp += 1
        message = conn.recv(1024)
        value = message.decode()
##        print(value)
        value_arr = [letter for letter in value]
        for letter in value_arr:
            if letter == "F":
                app = True
            elif letter == "#":
                app = False
##                loss = value.split("#\n")[-1]
                break

            if app == True:
                string += letter

        
##        value = value.rstrip()
##        print(value)
        if app == False and len(string) > 0:
            self.slider_update(string)
            string = ''


    def slider_update(self,received_data):

        slider_value = self.ui.verticalSlider.value()
        string_slider_value = str(slider_value)
        global servo_position

        servo_position = "X" + string_slider_value
        self.slider_gauge_progress(slider_value, received_data)

    def slider_gauge_progress(self, value, received_data):

        slider_label_stylesheet = """
color:white;
"""
        slider_stylesheet = """
border-radius: 55px;
	
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{LEVEL_1} rgba(255, 0, 127, 0), stop:{LEVEL_2} rgba(229, 132, 0, 255));

"""

        slider_text = """{SLIDER_VALUE}"""
        newtext = slider_text.replace("{SLIDER_VALUE}", str(value))
        self.ui.label.setText(newtext)
        level = (180-value)/180.0

        level_1 = str(level)
        level_2 = str(level+0.0018)
        #print(Oxy_1)
        #print("C")
        #print(Oxy_2)

        if level == 180:
            level_1 = "1.000"
            level_2 = "1.000"

        newsliderstyle = slider_stylesheet.replace("{LEVEL_1}", level_1).replace("{LEVEL_2}", level_2)
        self.ui.frame_19.setStyleSheet(newsliderstyle)
        
        self.update_data(received_data)
        
    def clear_graph(self):
        self.ui.waterflow_plot.clear()
        
    def update_data(self,received_data):

        arr = received_data.split('|')
        flow = arr[0]
        water_level = arr[1]
        temperature = arr[2]
        humidity = arr[3]

        flow_value = flow[1:]
        water_level_value = water_level[1:]
        temperature_value = temperature[1:]
        humidity_value = humidity[1:]
        
        if len(flow_value) <= 0:
            flow_value = '0'
        if len(water_level_value) <= 0:
            water_level_value = '0'
        if len(temperature_value) <= 0:
            temperature_value = '0'
        if len(humidity_value) <= 0:
            humidity_value = '0'

        print(flow_value + ' ' + water_level_value + ' ' + temperature_value + ' ' + humidity_value)
        
        
        flow_value_f = float(flow_value)
        water_level_value_f = float(water_level_value)
        temperature_value_f = float(temperature_value)
        humidity_value_f = float(humidity_value)
        
        if flow_value_f >= 100:
            flow_value_f = 100.0
        if water_level_value_f >= 100:
            water_level_value_f = 100.0
        if temperature_value_f >= 100:
            temperature_value_f = 100.0
        if humidity_value_f >= 100:
            humidity_value_f = 100.0

        global water_level_current, flow_rate_current, temperature_current, humidity_current, fault_time

        SMS_signal_stylesheet = """
        background-color: {COLOR};
        border-radius: 20px;
        """
        current_time = datetime.datetime.now()
        print(type(current_time))
        if water_level_value_f <= 5:
            send_SMS(flow_rate_current, water_level_current ,temperature_current, humidity_current, number)
            fault_time = datetime.datetime.now()
            
            
            new_SMS_signal_stylesheet = SMS_signal_stylesheet.replace("{COLOR}", "#ff9400")
            self.ui.SMS_signal.setStyleSheet(new_SMS_signal_stylesheet)
        time_diff = current_time - fault_time
        print(time_diff)
        if time_diff >= datetime.timedelta(seconds=30):
            new_SMS_signal_stylesheet = SMS_signal_stylesheet.replace("{COLOR}", "#1a222f")
            self.ui.SMS_signal.setStyleSheet(new_SMS_signal_stylesheet)
        

        water_level_current = int(water_level_value_f)
        temperature_current = int(temperature_value_f)
        humidity_current = int(humidity_value_f)
        flow_rate_current = int(flow_value_f)

        text_flow_stylesheet ="""
        background-color: None;
        color: white;

        """

        text_water_level_stylesheet ="""
        background-color: None;
        color: white;

        """

        text_temperature_stylesheet ="""
        background-color: None;
        color: white;

        """

        text_humidity_stylesheet ="""
        background-color: None;
        color: white;

        """

        html_flow_text = """{VALUE_flow}"""
        html_water_level_text = """{VALUE_water_level}"""
        html_temperature_text = """{VALUE_temperature}"""
        html_humidity_text = """{VALUE_humidity}"""
        
        if len(flow_value) > 0:
            newHtml_flow = html_flow_text.replace("{VALUE_flow}", str(int(flow_value_f)))
            self.ui.Flowrate.setText(newHtml_flow)

        if len(water_level_value) > 0:
            newHtml_water_level = html_water_level_text.replace("{VALUE_water_level}", str(int(water_level_value_f)))
            self.ui.Waterlevel.setText(newHtml_water_level)

        if len(temperature_value) > 0:
            newHtml_temperature = html_temperature_text.replace("{VALUE_temperature}", str(int(temperature_value_f)))
            self.ui.Temperature.setText(newHtml_temperature)

        if len(humidity_value) > 0:
            newHtml_humidity = html_humidity_text.replace("{VALUE_humidity}", str(int(humidity_value_f)))
            self.ui.Humidity.setText(newHtml_humidity)

        self.initiate_graph(flow_value_f, water_level_value_f, temperature_value_f, humidity_value_f)
        

    def initiate_graph(self, flow_value_f, water_level_value_f, temperature_value_f, humidity_value_f):

        self.waterflow_plot.show()
        self.timestamp += 1
        self.deque_timestamp.append(self.timestamp)
        self.deque_water_level.append(water_level_value_f)

        timeaxis_list = list(self.deque_timestamp)
        waterlevel_list = list(self.deque_water_level)

        if self.timestamp > self.graph_limit:
            self.waterflow_plot.setRange(xRange=[self.timestamp-self.graph_limit+1, self.timestamp], yRange=[0,100])
        self.set_plotdata(name="Water level", data_x=timeaxis_list,
                          data_y=waterlevel_list)
        
        self.gauge_indicator(flow_value_f, water_level_value_f, temperature_value_f, humidity_value_f)

    def set_plotdata(self, name, data_x, data_y):
        # print('set_data')
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            if name == "Water level":
                
                    self.traces[name] = self.waterflow_plot.getPlotItem().plot(pen=pg.mkPen((165,0, 255), width=2))

    #def update_graph(self, flow_value_f, water_level_value_f, temperature_value_f, humidity_value_f):

##        value = int(water_level_value_f)
##        
##        self.x = self.x[1:]  # Remove the first x element.
##        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
##
##        self.y = self.y[1:]  # Remove the first
##        self.y.append(value)  # Add a new value.
##
##        self.data_line.setData(self.x, self.y)
        
        #self.gauge_indicator(flow_value_f, water_level_value_f, temperature_value_f, humidity_value_f)
                
    def transmit(self):
        print("Transmit")
        self.ui.pushButton.clicked.connect(lambda: self.send_to_client(servo_position))


    def send_to_client(self, data):

        transmit_data = data.encode()
        conn.send(transmit_data)
        print("Sent")

    def gauge_indicator(self, flow, water_level, temperature, humidity):
        
        Flowrate_styleSheet = """
        QFrame{
	
border-radius: 110px;
	
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1_FLOW} rgba(255, 0, 127, 0), stop:{STOP_2_FLOW} rgba(85, 170, 255 , 255));
    
	
} """

        Water_level_styleSheet = """
        QFrame{
	
border-radius: 110px;
	
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1_WATER_LEVEL} rgba(255, 0, 127, 0), stop:{STOP_2_WATER_LEVEL} rgba(85, 170, 255 , 255));
    
	
} """

        flow_progress = (100-int(flow))/100.0
        stop_1_flow = str(flow_progress - 0.001)
        stop_2_flow = str(flow_progress)
        
        new_flowrate_Stylesheet = Flowrate_styleSheet.replace("{STOP_1_FLOW}", stop_1_flow).replace("{STOP_2_FLOW}", stop_2_flow)
        self.ui.FlowrateProgressBar.setStyleSheet(new_flowrate_Stylesheet)

        water_level_progress = (100-int(water_level))/100.0
        stop_1_water_level = str(water_level_progress - 0.001)
        stop_2_water_level = str(water_level_progress)
        
        new_water_level_Stylesheet = Water_level_styleSheet.replace("{STOP_1_WATER_LEVEL}", stop_1_water_level).replace("{STOP_2_WATER_LEVEL}", stop_2_water_level)
        self.ui.WaterlevelProgressBar.setStyleSheet(new_water_level_Stylesheet)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    sys.exit(app.exec_())

    
