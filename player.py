# Author: Sakib Chowdhury

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys
from paho.mqtt import client as mqtt_client
import time
import threading




class Window(QWidget):  


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Night")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('network.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
        self.init_ui()


    def init_ui(self):

        
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)



        #create video widget object
        videowidget = QVideoWidget()



        # create open button 
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        
        


        #create button or playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)



        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)



        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)



        #create hbox layout 
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)




        #add widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)




        #create vbox layout 
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)


        #mqtthandle
        


        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)


        #media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")


        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)


    
    def play_video(self):

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            

        else:
            self.mediaPlayer.play()


    def mediastate_changed(self, state):
        self.pos = self.mediaPlayer.position()
        print(self.pos)
        self.client.publish(self.topic, str(self.mediaPlayer.state())+ ";" + str(self.pos) + ";" + self.username)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )
            
        else :
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )
            



    def position_changed(self, position):
        self.slider.setValue(position)
        


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)




    def set_position(self, position):
        self.pos = position
        print(self.pos)
        self.mediaPlayer.setPosition(position)
        self.client.publish(self.topic, str(self.mediaPlayer.state())+ ";" + str(self.pos) + ";" + self.username)


    
    def connect_server(self):
        self.client.connect(self.broker, self.port)
        




    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def startServer(self, broker, port, username, password, topic):
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password
        self.topic = topic

        def on_connect(client, userdata, flags, rc):
            print("connected -rc: ", rc)

        def on_message(client, userdata, message):

            msg = message.payload.decode("utf-8")
            
            x = msg.split(";")
            print(x)
            state = int(x[0])
            pos = int(x[1])
            user = x[2]

            if user != self.username: 
                if state == QMediaPlayer.PlayingState:
                    self.mediaPlayer.play()
                else:
                    self.mediaPlayer.pause()
                
                self.mediaPlayer.setPosition(pos)

        def on_subscribe(client, userdata, mid, granted_qos):
            print("Subscribed: ", str(mid), str(granted_qos))

    
        self.pos = ""

        self.client = mqtt_client.Client()
        self.client.on_connect = on_connect
        self.client.on_subscribe = on_subscribe
        self.client.on_message = on_message
        self.client.username_pw_set(self.username, self.password)
        self.connect_server()
        self.client.subscribe(self.topic)
        self.client.loop_start()
        
